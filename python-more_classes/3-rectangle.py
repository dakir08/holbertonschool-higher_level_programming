#!/usr/bin/python3
"""
Rectangle class
"""


class Rectangle:
    """
    Constructor
    """
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    """
    Get width
    """
    @property
    def width(self):
        return self.__width

    """
    Set width
    """
    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    """
    Get height
    """
    @property
    def height(self):
        """Get/set the height of the rectangle."""
        return self.__height

    """
    Set width
    """
    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    """
    Calculate area of Rectangle.
    """
    def area(self):
        return self.__height * self.__width

    """
    Calculate perimeter of Rectangle object.
    """
    def perimeter(self):
        if self.__height == 0 or self.__width == 0:
            return 0
        return (self.__height + self.__width) * 2

    """
    Print rectangle
    """
    def __str__(self):
        if self.__width == 0 or self.__height == 0:
            return ("")

        rect = []
        for i in range(self.__height):
            for _ in range(self.__width):
                rect.append("#")
            rect.append("\n")

        print(rect)
        return "".join(rect)