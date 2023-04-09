#!/usr/bin/python3

"""
This module defines a Rectangle class that represents a rectangle.
"""


class Rectangle:
    """
    Represents a rectangle with a given width and height.

    Attributes:
        width (int): The width of the rectangle.
        height (int): The height of the rectangle.
    """

    def __init__(self, width=0, height=0):
        """
        Initializes a new Rectangle instance with the given width and height.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Gets or sets the width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        """Sets the width of the rectangle.

        Args:
            value (int): The width of the rectangle.

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Gets or sets the height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        """Sets the height of the rectangle.

        Args:
            value (int): The height of the rectangle.

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Calculates the area of the rectangle.

        Returns:
            The area of the rectangle.
        """
        return self.__width * self.__height

    def perimeter(self):
        """Calculates the perimeter of the rectangle.

        Returns:
            The perimeter of the rectangle.
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width * 2) + (self.__height * 2)

    def __str__(self):
        """Returns a printable string representation of the rectangle.

        Returns:
            A string representing the rectangle using '#' characters.
        """
        if self.__width == 0 or self.__height == 0:
            return ""

        rect = []
        for i in range(self.__height):
            [rect.append('#') for j in range(self.__width)]
            if i != self.__height - 1:
                rect.append("\n")
        return "".join(rect)
