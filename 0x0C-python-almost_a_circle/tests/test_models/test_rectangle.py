#!/usr/bin/python3
"""This module tests the Rectangle class in rectangle module"""
import unittest
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    '''In this class I will provide some testcases to test the rectangle'''
    def test_width(self):
        '''Check for value of width'''
        num = Rectangle(5, 6, 7, 8, 13)
        self.assertEqual(5, num.width)

    def test_height(self):
        '''Check for value of height'''
        num = Rectangle(5, 6, 7, 8, 13)
        self.assertEqual(6, num.height)

    def test_x(self):
        '''Check for value of x'''
        num = Rectangle(5, 6, 7, 8, 13)
        self.assertEqual(7, num.x)

    def test_y(self):
        '''Check for value of y'''
        num = Rectangle(5, 6, 7, 8, 13)
        self.assertEqual(8, num.y)

    def test_id(self):
        '''Check for value of id'''
        num = Rectangle(5, 6, 7, 8, 13)
        self.assertEqual(13, num.id)
