from .db import collabs
from typing import Any

def push_item(query: dict, key: str, value: Any) -> None:
    """Function for pushing an item to a key."""
    collabs.update(query, {'$push': {key: value}})