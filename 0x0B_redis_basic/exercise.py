#!/usr/bin/env python3
""" Writing strings to Redis """
import redis
import uuid


class Cache:
    """ Cache class """

    def __init__(self) -> None:
        """ Constructor """
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data) -> str:
        """ Store data in Redis"""
        key = str(uuid.uuid4())
        self._redis.set(key, data)

        return key
