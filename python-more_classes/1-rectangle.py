#!/usr/bin/python3
"""
Rectangle class
"""


class Rectangle:
    """Constructor"""
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    """Get width"""
    @property
    def width(self):
        return self.__width

    """Set width"""
    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    """Get height"""
    @property
    def height(self):
        """Get/set the height of the rectangle."""
        return self.__height

    """Set width"""
    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
