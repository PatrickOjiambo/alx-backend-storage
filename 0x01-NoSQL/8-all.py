#!/usr/bin/env python3
"""
File contains list_all
"""
from typing import List


def list_all(mongo_collection) -> List[dict]:
    """
    Lists all documents in a MongoDB collection.

    Parameters:
    - mongo_collection (Collection): The MongoDB collection to retrieve documents from.

    Returns:
    - List[dict]: A list containing dictionaries representing the documents in the collection.
    """
    if mongo_collection is not None:
        documents = mongo_collection.find()
        return [post for post in documents]
    return []
