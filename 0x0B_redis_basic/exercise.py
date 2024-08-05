#!/usr/bin/env python3
""" Writing strings to Redis """
import redis
import uuid
import functools
from typing import Union, Callable, Optional


def count_calls(method: Callable) -> Callable:
    """ Count calls decorator """
    @functools.wraps(method)
    def wrapper(self, *args, **kwargs):
        """ Wrapper that increments key every time the method is called """
        key = method.__qualname__
        self._redis.incr(key)

        return method(self, *args, **kwargs)
    return wrapper


def call_history(method: Callable) -> Callable:
    """ Call history decorator """
    @functools.wraps(method)
    def wrapper(self, *args, **kwargs):
        """ Wrapper that stores the history of inputs and outputs """
        input_key = f"{method.__qualname__}:inputs"
        output_key = f"{method.__qualname__}:outputs"

        self._redis.rpush(input_key, str(args))
        result = method(self, *args, **kwargs)
        self._redis.rpush(output_key, str(result))

        return result
    return wrapper


def replay(method: Callable):
    """ Display the history of calls for a particular function. """
    input_key = f"{method.__qualname__}:inputs"
    output_key = f"{method.__qualname__}:outputs"
    cache = method.__self__._redis

    inputs = cache.lrange(input_key, 0, -1)
    outputs = cache.lrange(output_key, 0, -1)

    print(f"{method.__qualname__} was called {len(inputs)} times:")
    for input_data, output_data in zip(inputs, outputs):
        input_str = input_data.decode('utf-8')
        output_str = output_data.decode('utf-8')
        print(f"{method.__qualname__}(*{input_str}) -> {output_str}")


class Cache:
    """ Cache class """

    def __init__(self) -> None:
        """ Constructor """
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
    @call_history
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """ Store data in Redis"""
        key = str(uuid.uuid4())
        self._redis.set(key, data)

        return key

    def get(self, key: str, fn: Optional[Callable] = None
            ) -> Optional[Union[str, bytes, int, float]]:
        """ Get data from Redis """
        data = self._redis.get(key)

        if data is None:
            return None
        if fn is None:
            return data

        return fn(data)

    def get_str(self, key: str) -> Optional[str]:
        """ Get a string """
        return self.get(key, lambda d: d.decode('utf-8'))

    def get_int(self, key: int) -> Optional[int]:
        """ Get an int """
        return self.get(key, int)
