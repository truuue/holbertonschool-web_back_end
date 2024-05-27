#!/usr/bin/python3
"""Basic dictionary"""

from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """ BasicCache inherits from BaseCaching """

    def put(self, key, item):
        """ put item in key cache """
        if key is not None or item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """get item from key cache"""
        return self.cache_data.get(key, None)
