#!/usr/bin/python3
""" FIFO cache """

from base_caching import BaseCaching


class FIFOCache(BaseCaching):

    def __init__(self):
        """Constructor"""
        super().__init__()
        self.queue = []

    def put(self, key, item):
        """put the item in key cache"""
        if key and item:
            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                first_key = self.queue.pop(0)
                del self.cache_data[first_key]
                print(f"DISCARD: {first_key}\n")
            self.queue.append(key)
            self.cache_data[key] = item

    def get(self, key):
        """get the item in key cache"""
        if key is None or key not in self.cache_data:
            return None
        else:
            self.cache_data(key)
