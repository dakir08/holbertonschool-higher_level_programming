#!/usr/bin/python3
"""
4-inherits_from.py
"""


def inherits_from(obj, a_class):
    """
    return boolean if the object is an instance of a inherited a_class
    """
    return isinstance(obj, a_class) and type(obj) is not a_class
