#!/usr/bin/python3
'''
This module for class MyList
'''


class MyList(list):
    '''This class inherits from list'''
    def print_sorted(self):
        '''This method print sorted list'''
        print(sorted(self))
