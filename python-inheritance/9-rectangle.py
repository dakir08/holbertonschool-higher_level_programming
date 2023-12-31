#!/usr/bin/python3
"""
Rectangle module.
"""


BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """
    Class Rectangle
    """

    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.integer_validator("height", height)

        self.__width = width
        self.__height = height

    def area(self):
        """
        return area of the rectangle
        """
        return self.__width * self.__height

    def __str__(self):
        """
        print friendly version of rectangle
        """
        return f"[Rectangle] {self.__width}/{self.__height}"
