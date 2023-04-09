def width(self):
     """Initializes a new Rectangle object.

    Args:
        width (int): The width of the new rectangle.
        height (int): The height of the new rectangle.
    """    
    return self.__width

    @width.setter
    """Returns the value of the width attribute."""
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Returns the value of the width attribute."""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

