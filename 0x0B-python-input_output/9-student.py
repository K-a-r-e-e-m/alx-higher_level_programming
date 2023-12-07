#!/usr/bin/python3
'''This module for Student class'''


class Student:
    '''This class defines a student'''
    def __init__(self, first_name, last_name, age):
        """This is the initialize method of class instances"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """This method retrieves a dictionary representation
        of a Student instance"""
        return self.__dict__
