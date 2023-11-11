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
