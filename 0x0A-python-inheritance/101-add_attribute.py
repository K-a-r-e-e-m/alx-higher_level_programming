#!/usr/bin/python
'''This module has add_attribute function that add new attr'''

def add_attribute(instance, name, value):
    """This function that adds a new attribute to an object"""

    if hasattr(instance, '__dict__'):
        setattr(instance, name, value)
    else:
        raise TypeError("can't add new attribute")

    '''
    Some objects, like built-in types (integers, strings, etc.),
    do not have a __dict__  because their attributes
    (e.g., integer values, string contents) are not stored in
    a dictionary-like structure.

    However, instances of custom classes in Python have a __dict__
    attribute by default. This __dict__ acts as a dictionary where
    Python stores the instance variables and their values.
    When you add a new attribute to an instance using
    setattr(instance, name, value), Python stores this attribute
    in instance.__dict__.

    This allows instances of custom classes to ```dynamically```
    add new attributes at runtime,
    which is not possible with built-in types.
    '''
