#!/usr/bin/python3
""" MRUCache """

from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """ MRUCache that inherits from BaseCaching """

    def __init__(self):
        """Constructor"""
        super().__init__()
        self.queue = []

    def put(self, key, item):
        self.cache_data[key] = item

        if key is None or item is None:
            return

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            discarded_key = self.queue.pop()
            del self.cache_data[discarded_key]
            print(f"DISCARD: {discarded_key}")

        self.queue.append(key)  # Add the key to the queue

    def get(self, key):
        """Get method for getting item in key"""
        if key is None or key not in self.cache_data:
            return None

        return self.cache_data[key]
