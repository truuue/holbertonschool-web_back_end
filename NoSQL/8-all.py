#!/usr/bin/env python3
"""Python function that lists all documents in a collection"""


def list_all(mongo_collection):
    """the listing function"""
    if mongo_collection is None:
        return []
    return mongo_collection.find()
