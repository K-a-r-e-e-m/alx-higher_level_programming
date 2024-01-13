#!/usr/bin/python3
"""This module for Rectangle class that inherits from Base"""
from models.base import Base


class Rectangle(Base):
    """This class for Rectangle"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """This is the intialization method of class"""
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        super().__init__(id)

    @property
    def width(self):
        '''This is width getter decorator'''
        return self.__width

    @width.setter
    def width(self, new_value):
        '''This is width setter decoratror'''
        self.__width = new_value

    @property
    def height(self):
        '''This is heigit getter decorator'''
        return self.__height

    @height.setter
    def height(self, new_value):
        '''This is heigit setter decoratror'''
        self.__height = new_value

    @property
    def x(self):
        '''This x width getter decorator'''
        return self.__x

    @x.setter
    def x(self, new_value):
        '''This is x setter decoratror'''
        self.__x = new_value

    @property
    def y(self):
        '''This is y getter decorator'''
        return self.__y

    @y.setter
    def y(self, new_value):
        '''This is y setter decoratror'''
        self.__y = new_value
