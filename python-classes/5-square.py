#!/usr/bin/python3
"""Define a Square class"""


class Square:
    """Constructor"""
    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size mustbe >= 0")
        self.__size = size

    """Return squared area"""
    def area(self):
        return self.__size ** 2

    """Get current size"""
    @property
    def size(self):
        return self.__size

    """Set current size"""
    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size mustbe >= 0")
        self.__size = value

    def my_print(self):
        """Print the square filled with #"""
        for _ in range(0, self.__size):
            for _ in range(self.__size):
                print("#", end="")
            print("")
        if self.__size == 0:
            print("")
