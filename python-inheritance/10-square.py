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
        self._size = size
        super().__init__(size, size)
