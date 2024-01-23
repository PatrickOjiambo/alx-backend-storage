#!/usr/bin/env python3
"""
 Python function that changes all topics of a school document based on the name:
"""
from typing import List


def update_topics(mongo_collection, name: str, topics: List[str]):
    """
    Python function that changes all topics of a school document based on the name:
    """
    what_to_update = {"name": name}
    after_update = {"$set": {"topics": topics}}
    mongo_collection.update_many(what_to_update, after_update)
