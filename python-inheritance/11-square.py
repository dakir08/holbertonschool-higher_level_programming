#!/usr/bin/python3
"""
Square module.
"""


Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """
    Class Square
    """

    def __init__(self, size):
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def __str__(self):
        """
        print friendly version of square
        """
        return f"[Square] {self.__size}/{self.__size}"
