#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    modified_list = my_list
    if 0 <= idx < len(my_list):
        modified_list[idx] = element
        return modified_list
    return my_list
