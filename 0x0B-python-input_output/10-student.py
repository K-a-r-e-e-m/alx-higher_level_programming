#!/usr/bin/python3
'''This module for Student class'''


class Student:
    '''This class defines a student
    '''
    def __init__(self, first_name, last_name, age):
        """This is the initialize method of class instances
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """This method retrieves a dictionary representation
        of a Student instance
        """
        if (type(attrs) is list and all(type(itm) is str for itm in attrs)):
            return {n: getattr(self, n) for n in attrs if hasattr(self, n)}

        return self.__dict__


# The all() function checks each element in the iterable and
# returns False if any element evaluates to False.
# If all elements are True or the iterable is empty, it returns True.

# getattr(object, name[, default]): This function returns
# the value of an attribute of an object

# hasattr(object, name): This function checks
# whether an object has a certain attribute.
