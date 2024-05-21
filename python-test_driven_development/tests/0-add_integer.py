#!/usr/bin/python3

def add_integer(a, b=98):
    """
    add two integers of float casted to integers.

    Parameters:
    a (int or float): the frist number.
    b (int or float): the seconde number, default is 98.

    Return:
    int: The sum of a and b casted to integers.

    Raises:
    TypeError: If a or b are not integers or float.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)

if __name__ == "__main__":
    import doctest
    doctest.testmod(add_integer.txt)
