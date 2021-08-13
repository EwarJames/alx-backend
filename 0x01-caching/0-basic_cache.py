#!/usr/bin/env python3
"""Implements Python caching"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """Dictinary cache"""

    def put(self, key, item):
        """Puts items into the cache"""
        if key is None or item is None:
            pass
        else:
            self.cache_data(key) = item

    def get(self, key):
        """Gets an item by key"""
        return self.cache_data.get(key)
