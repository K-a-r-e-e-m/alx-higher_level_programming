#!/usr/bin/python3
"""This Module has the child class thad drieved from parent class"""
from models.rectangle import Rectangle


class Square(Rectangle):
    '''This class inherit from Rectangle class'''

    def __init__(self, size, x=0, y=0, id=None):
        '''Constructor method that has special functino super()'''
        super().__init__(size, size, x, y, id)

    def __str__(self):
        '''String representation of instance'''
        return f'[Square] ({self.id}) {self.x}/{self.y} - {self.width}'

    @property
    def size(self):
        '''Getter for size'''
        return self.width

    @size.setter
    def size(self, newSize):
        '''Setter for size'''
        if type(newSize) is not int:
            raise TypeError('width must be an integer')
        if newSize <= 0:
            raise ValueError('width must be > 0')
        self.width = newSize
        self.height = newSize
