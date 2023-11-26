#!/usr/bin/python3
"""
8. Class to JSON
"""


def class_to_json(obj):
    """
    Return dictionary description for class
    """
    return obj.__dict__
