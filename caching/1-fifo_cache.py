#!/usr/bin/python3
"""FIFO Cache"""
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """FIFOCache class that inherits from BaseCaching"""
    def __init__(self):
        super().__init__()
        self.queue = []

    def put(self, key, item):
        """put method for put item in key"""
        if key is None or item is None:
            return

        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            first_key = self.queue.pop(0)
            del self.cache_data[first_key]
            print(f"DISCARD: {first_key}\n")

        self.queue.append(key)
        self.cache_data[key] = item

    def get(self, key):
        """get method for getting item in key"""
        if key is None or key not in self.cache_data:
            return None

        return self.cache_data[key]
