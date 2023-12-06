#!/usr/bin/python3
"""
Rectangle Module
"""


from models.base import Base


class Rectangle(Base):
    """
    Rectangle class
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Initialize a new Rectangle.
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """
        Get rectangle width.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Set rectangle width.
        """
        self.__width = value

    @property
    def height(self):
        """
        Get rectangle height.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Set rectangle height.
        """
        self.__height = value

    @property
    def x(self):
        """
        Get x coordinator of the rectangle.
        """
        return self.__x

    @x.setter
    def x(self, value):
        """
        Set x coordinator of the rectangle.
        """
        self.__x = value

    @property
    def y(self):
        """
        Get y coordinator of the rectangle.
        """
        return self.__y

    @y.setter
    def y(self, value):
        """
        Set y coordinator of the rectangle.
        """
        self.__y = value
