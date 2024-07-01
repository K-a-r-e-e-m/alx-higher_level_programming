#!/usr/bin/python3
'''This module for a Rectangle class'''
superRectangle = __import__('9-rectangle').Rectangle


class Square(superRectangle):
    '''Rectangel calss inherit from BaseGeometry class'''

    def __init__(self, size):
        self.__size = size
        self.integer_validator("size", size)
        super().__init__(size, size)

    def __str__(self):
        return f'[Square] {self.__size}/{self.__size}'
