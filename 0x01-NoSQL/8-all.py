"""
Python function that lists all documents in a collection:
"""
from typing import List
from pymongo.collection import Collection
from typing import List
from pymongo.collection import Collection


def list_all(mongo_collection: Collection) -> List[dict]:
    """
    Python function that lists all documents in a collection:
    """
    if mongo_collection is not None:
        documents = mongo_collection.find()
        return [post for post in documents]
    return []
