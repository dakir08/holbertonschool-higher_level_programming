#!/usr/bin/python3
"""
BaseGeometry module.
"""


class BaseGeometry:
    """
    Class BaseGeometry
    """

    def area(self):
        """
        Implementation later
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validate integer with exception
        """
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
