#!/usr/bin/python3
'''This module check for is obj is same class or not'''


def is_kind_of_class(obj, a_class):

    '''This function returns True if the object is an instance
    of the specified class ; otherwise False. '''

    return isinstance(obj, a_class)
