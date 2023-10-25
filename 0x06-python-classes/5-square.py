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
        self.__size = size

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

    def area(self):
        """Return The current square area"""
        return self.__size ** 2

    def my_print(self):
        """Print a square with '#' character"""
        if self.__size == 0:
            print()
        else:
            # First solution BEST SOLUTION
            for i in range(self.__size):
                print('#' * self.__size)
            # Second solution with using LIST COMPREHENTION
            '''
            for i in range(self.__size):
                [print('#', end='') for j in range(self.__size)]
                print()
            '''
            # Third solution OBIVIOUS SOLUTION
            '''
            for i in range(self.__size):
                for j in range(self.__size):
                    print('#',end='')
                print()
            '''
