#!/usr/bin/python3
'''This module for a MyInt class'''


class MyInt(int):
    '''MyInt is a rebel. MyInt has == and != operators inverted'''

    def __init__(self, first):
        self.first = first

    def __eq__(self, second):
        if (self.first == second):
            return False

    def __ne__(self, second):
        if (self.first == second):
            return True
