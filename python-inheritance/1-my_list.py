#!/usr/bin/python3
'''
1-my_list.py
'''


class MyList(list):
    '''
    MyList class
    '''

    def print_sorted(self):
        '''
        print the sorted list
        '''
        print(sorted(self))
