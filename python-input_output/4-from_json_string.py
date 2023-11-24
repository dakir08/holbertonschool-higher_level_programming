#!/usr/bin/python3
"""
4. From JSON string to Object
"""


import json


def from_json_string(my_str):
    """
    convert string to json object
    """
    return json.loads(my_str)
