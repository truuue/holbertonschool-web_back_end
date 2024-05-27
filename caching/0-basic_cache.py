#!/usr/bin/python3
"""Basic dictionary"""

from base_caching import BaseCaching


class BasicCache(BaseCaching):

    def __init__(self):
        self.cache_data = {}

    def put(self, key, item):
        self.cache_data[key] = item

        if key is None:
            pass
        if item is None:
            pass

    def get(self, key):

        if key is None or key not in self.cache_data:
            return None
        return self.cache_data.get(key)
