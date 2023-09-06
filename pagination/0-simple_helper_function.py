#!/usr/bin/env python3
"""function named index_range that takes two integer arguments page and page_size"""


def index_range(page: int, page_size: int) -> list:
    """index_range function"""
    return ((page - 1) * page_size, ((page - 1) * page_size) + page_size)
