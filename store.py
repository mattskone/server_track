"""
A simple, in-memory data store.
"""

_store = {}


def add_item(item_name, item):
    """Add an item to the data store.

    If item_name already exists, add item to an existing list of items for
    item_name.
    """

    if item_name in _store.keys():
        _store[item_name].append(item)
    else:
        _store[item_name] = [item]


def get_item(item_name):
    """Return a list of stored data for item_name.
    
    Returns None item_name does not exist.
    """

    try:
        return _store[item_name]
    except KeyError:
        return None

