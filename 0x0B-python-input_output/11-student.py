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
            return {ky: getattr(self, ky) for ky in attrs if hasattr(self, ky)}

        return self.__dict__

    def reload_from_json(self, json):
        """This method replaces all attributes of the Student instance
        """
        for key, value in json.items():
            setattr(self, key, value)


# The all() function checks each element in the iterable and
# returns False if ''any'' element evaluates to False.
# If all elements are True or the iterable is empty, it returns True.

# getattr(object, name[, default]): This function returns
# the ''value'' of an attribute of an object

# hasattr(object, name): This function checks
# whether an object ''has'' a certain attribute.

# setattr() is a built-in Python function that sets
# the value of a specified attribute of an object.
# It takes three parameters: the object,
# the attribute name, and the value to set.

# items() function is used with dictionaries to return a view object
# that displays a list of a dictionary's key-value pairs as tuples.
# my_dict = {'a': 1, 'b': 2, 'c': 3}
# items = my_dict.items()
# print(items)
# Output: dict_items([('a', 1), ('b', 2), ('c', 3)])
