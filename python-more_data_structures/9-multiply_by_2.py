#!/usr/bin/python3
def multiply_by_2(my_dict: dict):
    cloned_dict = my_dict.copy()
    for x in cloned_dict.keys():
        cloned_dict[x] *= 2
    return cloned_dict
