#!/usr/bin/python3
"""This module for Rectangle class that inherits from Base"""
from base import Base 


class Rectangle(Base):
    """This class for Rectangle"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """This is the intialization method of class"""
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
