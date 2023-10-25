#!/usr/bin/python3
"""This class defines a square by: (based on 0-square.py)"""


class Square:
    """Exmaple of docstring.

    This class for represent the square
    """
    def __init__(self, size=0):
        """Intialize square
        Args:
            size (int): size of square private instance attribute.
        """
        # The isinstance() is a built-in function used for type checking
        # It verifies if an object is of a specified type
        # returning True if it is, and False otherwise.
        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')
        self.__size = size

    def area(self):
        """Return The current square area"""
        return self.__size ** 2
