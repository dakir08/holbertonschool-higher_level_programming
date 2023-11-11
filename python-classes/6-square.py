#!/usr/bin/python3
"""Define a Square class"""


class Square:
    """Constructor"""
    def __init__(self, size=0, position=(0, 0)):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size mustbe >= 0")
        self.__size = size
        if (not isinstance(position, tuple) or
                len(position) != 2 or
                not self.contains_only_integers(position) or
                not self.only_positive_integers(position)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = position

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

    """Print the square filled with #"""
    def my_print(self):
        # no size
        if self.__size == 0:
            print("")
            return
        # print empty line
        for _ in range(0, self.__position[1]):
            print("")
        for _ in range(0, self.__size):
            # print space for left over postion
            for _ in range(0, self.__position[0]):
                print(" ", end="")
                # print #
            for _ in range(self.__size):
                print("#", end="")
            print("")
        if self.__size == 0:
            print("")

    """Get current position"""
    @property
    def position(self):
        return (self.__position)

    """Set current position"""
    @position.setter
    def position(self, value):
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not self.contains_only_integers(value) or
                not self.only_positive_integers(value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def contains_only_integers(tuple):
        return all(isinstance(value, int) for value in tuple)

    def only_positive_integers(tuple):
        return all(num >= 0 for num in tuple)
