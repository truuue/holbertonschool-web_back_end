#!/usr/bin/python3
""" LRUCache """

from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """ LRUCache class that inherits from BaseCaching """

    def __init__(self):
        """Constructor"""
        super().__init__()
        self.queue = []

    def put(self, key, item):
        """Put method"""
        if key is None or item is None:
            return

        self.cache_data[key] = item

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            discard_key = self.queue.pop(0)
            del self.cache_data[discard_key]
            print(f"DISCARD: {discard_key}")

        if key in self.queue:
            self.queue.remove(key)
        self.queue.append(key)

    def get(self, key):
        """Get method for getting item in key"""
        if key in self.queue:
            self.queue.remove(key)
            self.queue.append(key)

        if key is None or key not in self.cache_data:
            return None
        else:
            return self.cache_data[key]
