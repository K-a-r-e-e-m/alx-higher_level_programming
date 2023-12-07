#!/usr/bin/python3
'''This module for a BaseGeometry class'''


class BaseGeometry:
    '''This is a BaseGeometry class'''

    def area(self):
        '''This method for area'''
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        '''This method for validate value'''
        if type(value) is not int:
            raise TypeError('{} must be an integer'.format(name))
        if value <= 0:
            raise ValueError('{} must be greater than 0'.format(name))
