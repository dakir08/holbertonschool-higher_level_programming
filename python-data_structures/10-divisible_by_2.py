#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    list = my_list.copy()
    for index, num in enumerate(my_list):
        if num % 2 == 0:
            list[index] = True
        else:
            list[index] = False
    return list
