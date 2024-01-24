#!/usr/bin/env python3
"""
Task 0
"""
from typing import Union
import uuid
from uuid import UUID
import redis


class Cache:
    """
    Cache class
    """

    def __init__(self) -> None:
        """
        constructor for the class
        """
        self._redis = redis.Redis(decode_responses=True)
        self._redis.flushdb(True)

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        Takes a data argument and returns
        the random generated key.
        """
        randkey: str = str(uuid.uuid4())
        self._redis.set(randkey, data)
        return randkey
