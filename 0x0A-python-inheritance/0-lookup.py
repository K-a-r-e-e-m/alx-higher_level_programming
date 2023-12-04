#!/usr/bin/python3
'''
This module is a function that returns the list of available
attributes and methods of an object.
'''


def lookup(obj):
    '''This function return list of availabe attributes and method'''
    return dir(obj)
