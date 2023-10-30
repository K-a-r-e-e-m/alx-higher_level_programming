#!/usr/bin/python3
"""This class defines a rectangle"""


class Rectangle:
    """Docstring of rectangle class"""
    def __init__(self, width=0, height=0):
        """Initialize the rectangle.

        Args:
            width (int): The width of rectangle
            height (int): The height of rectangle
        """
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """This is getter function that return the width"""
        return self.__width

    @width.setter
    def width(self, value):
        """This is setter function that set a new value of width"""
        if type(value) is not int:
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value

    @property
    def height(self):
        """This is getter function that return the height"""
        return self.__height

    @height.setter
    def height(self, value):
        """This is setter function that set a new value of height"""
        if type(value) is not int:
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value
