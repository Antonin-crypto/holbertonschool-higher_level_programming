#!/usr/bin/python3
"""contient the code python"""


class Square:
    """contient the class of python"""
    # isinstance(objet, type) function returns True if the specified object
    # is of the specified type, otherwise False
    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Calcule et retourne l'aire du carré."""
        return self.size ** 2
