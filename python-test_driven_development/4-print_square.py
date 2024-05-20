#!/usr/bin/python3
"""prints a square with the character #"""


def print_square(size):
    """prints a square with the character #
    return an error if size it's not integer
    of if size less than 0"""
    if isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")
    if not isinstance(size, (int)):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    print("{}".format(("#" * size + "\n") * size), end="")
