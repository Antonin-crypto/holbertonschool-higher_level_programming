#!/usr/bin/python3
""" Definition of inherits_from function"""


def inherits_from(obj, a_class):
    """
    Check if the object is an instance of a class that inherited
    (directly or indirectly)
    from the specified class.

    Args:
        obj: The object to check.
        a_class: The class to check against.

    Returns:
        True if the object is an instance of a class that inherited
        from the specified class,
        otherwise False.
    """
    if type(obj) is a_class:
        return False
    else:
        return isinstance(obj, a_class)
