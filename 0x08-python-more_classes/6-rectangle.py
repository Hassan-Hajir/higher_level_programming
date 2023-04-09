#!/usr/bin/python3
"""
This module defines a Rectangle class.
"""


class Rectangle:
    """
    Represents a rectangle.

    Attributes:
        number_of_instances (int): The number of Rectangle instances.
    """
    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """
        Initializes a new Rectangle instance.

        Args:
            width (int): The width of the new rectangle.
            height (int): The height of the new rectangle.
        """
        type(self).number_of_instances += 1
        self._width = width
        self._height = height

    @property
    def width(self):
        """Get or set the width of the Rectangle."""
        return self._width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self._width = value

    @property
    def height(self):
        """Get or set the height of the Rectangle."""
        return self._height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self._height = value

    def area(self):
        """Returns the area of the Rectangle."""
        return (self._width * self._height)

    def perimeter(self):
        """Returns the perimeter of the Rectangle."""
        if self._width == 0 or self._height == 0:
            return 0
        return (self._width * 2) + (self._height * 2)

    def __str__(self):
        """Returns a string representation of the Rectangle."""
        if self._width == 0 or self._height == 0:
            return ""

        rect = []
        for i in range(self._height):
            [rect.append('#') for j in range(self._width)]
            if i != self._height - 1:
                rect.append("\n")
        return "".join(rect)

    def __repr__(self):
        """Returns a string representation of the Rectangle."""
        rect = f"Rectangle({self._width}, {self._height})"
        return rect

    def __del__(self):
        """Prints a message for every deletion of a Rectangle."""
        type(self).number_of_instances -= 1
        print("Bye rectangle...")
