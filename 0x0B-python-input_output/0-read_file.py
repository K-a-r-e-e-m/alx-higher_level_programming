#!/usr/bin/python3
'''This module for input and output files in python '''

def read_file(filename=""):
    '''This method for read file'''
    with open(filename) as f:
        print(f.read())
