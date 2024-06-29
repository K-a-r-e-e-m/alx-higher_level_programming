#!/usr/bin/python3
"""This class defines a rectangle"""


class Rectangle:
    """Docstring of rectangle class"""

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Initialize the rectangle.
        Args:
            width (int): The width of rectangle
            height (int): The height of rectangle
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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
        """Draw a rectangle with specified character"""
        draw = ''
        for x in range(self.__height):
            draw += str(self.print_symbol) * self.__width
            if x != self.__height - 1 and self.__width and self.__height:
                draw += '\n'
        return draw

    def __repr__(self):
        """Return the string representaion of the object"""
        return f"{self.__class__.__name__}({self.width}, {self.height})"

    def __del__(self):
        """Print msg when instance is deleted"""
        print('Bye rectangle...')
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Static method that make a logical connection with class 
        not Depend on it attributes or methods"""
        if not isinstance(rect_1, Rectangle):
            raise TypeError('rect_1 must be an instance of Rectangle')
        if not isinstance(rect_2, Rectangle):
            raise TypeError('rect_2 must be an instance of Rectangle')

        if rect_1.area() > rect_2.area():
            return rect_1
        elif rect_2.area() > rect_1.area():
            return rect_2
        else:
            return rect_1
