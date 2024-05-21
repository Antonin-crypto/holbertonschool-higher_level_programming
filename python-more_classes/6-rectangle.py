#!/usr/bin/python3
"""Defines a Python class """


class Rectangle:
    """Represents a rectangle with width and height attributes."""
    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """Initializes a Rectangle instance with given width and height.

        Args:
            width (int): The width of the rectangle. Default is 0.
            height (int): The height of the rectangle. Default is 0.
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """Getter for the width attribute.

        Returns:
            int: The width of the rectangle.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """Setter for the width attribute.

        Args:
            value (int): The width to set for the rectangle.

        Raises:
            TypeError: If width is not an integer.
            ValueError: If width is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Getter for the height attribute.

        Returns:
            int: The height of the rectangle.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """Setter for the height attribute.

        Args:
            value (int): The height to set for the rectangle.

        Raises:
            TypeError: If height is not an integer.
            ValueError: If height is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Calculates the area of the rectangle.

        Returns:
            int: The area of the rectangle.
        """
        return self.width * self.height

    def perimeter(self):
        """Calculates the perimeter of the rectangle.

        Returns:
            int: The perimeter of the rectangle, or 0 if width or height is 0.
        """
        if self.width == 0 or self.height == 0:
            return 0
        return 2 * (self.width + self.height)

    def __str__(self):
        """Returns a string representation of the rectangle.

        Returns:
            str: A string representation of the rectangle using '#' to represen
            each cell in the rectangle.
        """
        if self.width == 0 or self.height == 0:
            return ''
        rectangle = ''
        for i in range(self.height):
            rectangle += '#' * self.width + '\n'
        return rectangle[:-1]

    def __repr__(self):
        """Returns a string representation of the rectangle.

    Returns:
        str: A string representation of the rectangle that can be used to
        recreate the object.
    """
        return "Rectangle({}, {})".format(self.width, self.height)

    def __del__(self):
        """Destructor method for the Rectangle class.

    Prints a message indicating the deletion of the object.
    """
        print("Bye rectangle...")
