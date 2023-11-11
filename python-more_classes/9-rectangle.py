#!/usr/bin/python3
"""
Module Rectangle
"""


class Rectangle:
    """Rectangle class"""
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """
        Constructor
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @classmethod
    def square(cls, size=0):
        """
        Create a Rectangle with width = height = size
        """
        return cls(size, size)

    @property
    def width(self):
        """
        Get width
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Set width
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        Get height
        """
        """Get/set the height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        """
        Set width
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """
        Calculate area of Rectangle.
        """
        return self.__height * self.__width

    def perimeter(self):
        """
        Calculate perimeter of Rectangle object.
        """
        if self.__height == 0 or self.__width == 0:
            return 0
        return (self.__height + self.__width) * 2

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """
        Return the comparison between 2 rectangle.
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        return rect_1 if rect_1.area() >= rect_2.area() else rect_2

    def __str__(self):
        """
        Return rectangle with print_symbol
        """
        if self.__width == 0 or self.__height == 0:
            return ("")
        rect = ""
        for i in range(self.__height):
            for _ in range(self.__width):
                rect += str(self.print_symbol)
            if i != self.__height - 1:
                rect += "\n"
        return "".join(rect)

    def __repr__(self):
        """
        Return represenation of the rectangle
        """
        rect = f"Rectangle({self.__width}, {self.height})"
        return rect

    def __del__(self):
        """
        Delete rectangle
        """
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
