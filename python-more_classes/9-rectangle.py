#!/usr/bin/python3
"""Defines a Python class """


class Rectangle:
    """Represents a rectangle with width and height attributes."""
    number_of_instances = 0
    print_symbol = "#"

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
            rectangle += str(self.print_symbol) * self.width + '\n'
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

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Compares two Rectangle objects and returns the one with the larger
        area.

    Args:
        rect_1 (Rectangle): The first rectangle to compare.
        rect_2 (Rectangle): The second rectangle to compare.

    Raises:
        TypeError: If either rect_1 or rect_2 is not an instance of Rectangle.

    Returns:
        Rectangle: The rectangle object with the larger area,
        or rect_2 if areas are equal.
    """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")

        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2

    @classmethod
    def square(cls, size=0):
        """Creates a square Rectangle object with equal width and height.

    Args:
        cls: The class (Rectangle).
        size (int): The size of the square (both width and height). Default is
        0.

    Returns:
        Rectangle: A square rectangle object with equal width and height.
    """
        return cls(size, size)
