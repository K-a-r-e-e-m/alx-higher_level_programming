#!/usr/bin/python3
"""This class defines a square by: (based on 0-square.py)"""


class Square:
    """Exmaple of docstring.

    This class for represent the square
    """
    def __init__(self, size=0, position=(0, 0)):
        """Intialize square
        Args:
            size (int): size of square private instance attribute.
        """
        self.__size = size
        self.__position = position

    @property
    def size(self):
        """Retrieve the size (getter)"""
        return self.__size

    @size.setter
    def size(self, value):
        """Set value to size (setter)"""
        # The isinstance() is a built-in function used for type checking
        # It verifies if an object is of a specified type
        # returning True if it is, and False otherwise.
        if not isinstance(value, int):
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    @property
    def position(self):
        """Retrieve the position (getter)"""
        return self.__position

    @position.setter
    def position(self, value):
        """Set the value of postion (setter)"""
        if (
            not isinstance(value, tuple)
            or len(value) != 2
            or len([i for i in value if isinstance(i, int) and i > 0]) != 2
           ):
            raise TypeError('position must be a tuple of 2 positive integers')
        else:
            self.__position = value

    def area(self):
        """Return The current square area"""
        return self.__size ** 2

    def my_print(self):
        """Print a square with '#' character"""
        if self.__size == 0:
            print()
        else:
            [print() for i in range(self.__position)]

            for i in range(self.__size):
                [print(' ', end='') for j in range(self.__position[0])]
                [print('#', end='') for k in range(self.__size)]
                print()
