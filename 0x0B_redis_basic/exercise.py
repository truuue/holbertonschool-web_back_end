#!/usr/bin/env python3
""" Writing strings to Redis """
import redis
import uuid
import functools
from typing import Union, Callable, Optional


def count_calls(method: Callable) -> Callable:
    @functools.wraps(method)
    def wrapper(self, *args, **kwargs):
        key = method.__qualname__
        self._redis.incr(key)

        return method(self, *args, **kwargs)
    return wrapper


class Cache:
    """ Cache class """

    def __init__(self) -> None:
        """ Constructor """
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """ Store data in Redis"""
        key = str(uuid.uuid4())
        self._redis.set(key, data)

        return key

    def get(self, key: str, fn: Optional[Callable] = None) -> Optional[Union[str, bytes, int, float]]:
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
