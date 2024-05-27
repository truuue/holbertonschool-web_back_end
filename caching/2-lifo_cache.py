#!/usr/bin/python3
""" LIFOCache """

from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """ LIFOCache class that inherits from BaseCaching """

    def __init__(self):
        """constructor"""
        super().__init__()
        self.queue = []

    def put(self, key, item):
        """put method"""
        if key is None or item is None:
            return

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            discarded_key = self.queue.pop()
            del self.cache_data[discarded_key]
            print(f"DISCARD: {discarded_key}")

        self.cache_data[key] = item
        self.queue.append(key)

    def get(self, key):
        """get method for getting item in key"""
        if key is None or key not in self.cache_data:
            return None

        return self.cache_data[key]
