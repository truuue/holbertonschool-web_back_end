#!/usr/bin/python3
"""Basic dictionary"""

from base_caching import BaseCaching


class BasicCache(BaseCaching):

    def put(self, key, item):
        if key is not None or item is not None:
            self.cache_data[key] = item

    def get(self, key):
        return self.cache_data.get(key)
