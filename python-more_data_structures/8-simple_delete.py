#!/usr/bin/python3
def simple_delete(my_dict: dict, key=""):
    if my_dict.get(key) is not None:
        del my_dict[key]
    return my_dict
