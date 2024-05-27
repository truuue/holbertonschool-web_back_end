#!/usr/bin/python3
""" FIFO cache """

from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    def put(self, key, item):
        if key is not None or item is not None:
            self.cache_data[key] = item

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            first_key = next(iter(self.cache_data))
            del self.cache_data[first_key]
            print(f"DISCARD: {first_key}")

    def get(self, key):
        if key is None or key not in self.cache_data:
            return None
        else:
            self.cache_data(key)
