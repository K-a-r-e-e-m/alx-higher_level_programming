#!/usr/bin/python3
"""This module for append function"""


def append_write(filename="", text=""):
    """This function appends a string at the end of a text file
    and returns the number of characters added
    """
    with open(filename, 'a', encoding='utf-8') as file:
        number_added = file.write(text)

    return number_added
