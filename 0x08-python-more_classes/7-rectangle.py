#!/usr/bin/python3

"""
This module defines the Rectangle class.
"""


class Rectangle:
    """
    A class used to represent a rectangle.

    Attributes:
        number_of_instances (int): The number of Rectangle instances.
        print_symbol (any): The symbol used for string representation.
    """
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """
        Constructs all the necessary attributes for the Rectangle object.

        Args:
            width (int): The width of the new rectangle.
            height (int): The height of the new rectangle.
        """
        type(self).number_of_instances += 1
        self.width = width
        self.height = height

    @property
    def width(self):
        """
        Getter method for width.

        Returns:
            The width of the Rectangle object.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Setter method for width.

        Args:
            value (int): The width of the Rectangle object.

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is less than zero.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        Getter method for height.

        Returns:
            The height of the Rectangle object.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Setter method for height.

        Args:
            value (int): The height of the Rectangle object.

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is less than zero.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """
        Calculates the area of the Rectangle object.

        Returns:
            The area of the Rectangle object.
        """
        return self.__width * self.__height

    def perimeter(self):
        """
        Calculates the perimeter of the Rectangle object.

        Returns:
            The perimeter of the Rectangle object.
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """
        Returns a string representation of the Rectangle object.

        Returns:
            A string rep of the object using the print_symbol attribute.
        """
        if self.__width == 0 or self.__height == 0:
            return ""
        rect = []
        for i in range(self.__height):
            [rect.append(str(self.print_symbol)) for j in range(self.__width)]
            if i != self.__height - 1:
                rect.append("\n")
        return "".join(rect)

    def __repr__(self):
        """
        Returns a string representation of the Rectangle object.

        Returns:
            A string representation of the Rectangle object.
        """
        return f'Rectangle({self.__width}, {self.__height})'

    def __del__(self):
        """
        Deletes the object and decrements number_of_instances attribute.
        """
        type(self).number_of_instances -= 1
        print("Bye rectangle...")
