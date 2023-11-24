#!/usr/bin/python3
"""
1. Write to a file
"""


def write_file(filename="", text=""):
    """ 
    write a string to a text file and
    return the number of characters written 
    """
    with open(filename, 'w') as f:
        return f.write(text)
