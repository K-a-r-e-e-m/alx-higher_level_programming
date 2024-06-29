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
        self.width = width
        self.height = height

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

    def area(self):
        """This method calculate the area of recatangle"""
        return self.__width * self.__height

    def perimeter(self):
        """This method calculate the perimeter"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width + self.__height) * 2

    def __str__(self):
        """Draw a rectangle with # character"""
        draw = ''
        for x in range(self.__height):
            for i in range(self.__width):
                draw += '#'
            if x != self.__height - 1 and self.__width and self.__height:
                draw += '\n'
        return draw

    def __repr__(self):
        """Return the string representaion of the object
        as python code, we can evaluate the code by eval() """
        return f"{self.__class__.__name__}({self.width}, {self.height})"
