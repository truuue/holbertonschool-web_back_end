#!/usr/bin/python3
""" LRUCache """

from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """ MRUCache class that inherits from BaseCaching """

    def __init__(self):
        """constructor"""
        super().__init__()

    def put(self, key, item):
        """put method"""
        if key is None or item is None:
            return

        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            discard_key = max(self.cache_data, key=self.cache_data.get)
            del self.cache_data[discard_key]
            print("DISCARD:", discard_key)

        self.cache_data[key] = item

    def get(self, key):
        """get method for getting item in key"""
        if key is None or key not in self.cache_data:
            return None

        return self.cache_data[key]
