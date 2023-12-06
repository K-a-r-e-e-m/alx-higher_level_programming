#!/usr/bin/python3
"""This module for write in file"""


def write_file(filename="", text=""):
    """This function writes a string to a text file
    and returns the number of characters
    """
    with open(filename, 'w', encoding='utf-8') as f:
        num = f.write(text)

    return num
