#!/usr/bin/python3
""" LRUCache """

from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """ LRUCache class that inherits from BaseCaching """

    def __init__(self):
        """constructor"""
        super().__init__()
        self.queue = []

    def put(self, key, item):
        """put method"""
        if key is None or item is None:
            return

        if key in self.cache_data:
            self.queue.remove(key)
        elif len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            discard_key = self.queue.pop(0)
            del self.cache_data[discard_key]
            print("DISCARD:", discard_key)

        self.queue.append(key)
        self.cache_data[key] = item

    def get(self, key):
        """get method for getting item in key"""
        if key is None or key not in self.cache_data:
            return

        return self.cache_data[key]
