"""
Python function that lists all documents in a collection:
"""


def list_all(mongo_collection):
    """
    Python function that lists all documents in a collection:
    """
    if mongo_collection is not None:
        documents = mongo_collection.find()
        return [post for post in documents]
    return []
