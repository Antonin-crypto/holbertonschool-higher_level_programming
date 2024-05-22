#!/usr/bin/python3
"""function that returns the list of available attributes"""


def lookup(obj):
    """Returns the list of available attributes for the given object.

    Args:
        obj: The object to inspect.

    Returns:
        A list of strings representing the available attributes of the object.
    """
    return dir(obj)
