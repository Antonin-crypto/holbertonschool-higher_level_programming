#!/usr/bin/python3
""" Class BaseGemotry"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """class Square that inherits from Rectangle"""
    def __init__(self, size):
        """Initialize size after validation"""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """Return the area of the rectangle"""
        return self.__size * self.__size

    def __str__(self):
        """Return the string representation of the rectangle"""
        return "[Square] {:d}/{:d}".format(self.__size, self.__size)
