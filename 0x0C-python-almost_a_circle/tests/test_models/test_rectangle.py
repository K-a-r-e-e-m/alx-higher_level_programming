#!/usr/bin/python3
"""This module tests the Rectangle class in rectangle module"""
import unittest
from models.rectangle import Rectangle
from models.base import Base


class TestRectangle(unittest.TestCase):
    '''In this class I will provide some testcases to test the rectangle'''
    def test_inheritance(self):
        '''Check for inheritance of class'''
        self.assertIsInstance(Rectangle(2, 5), Base)

    def test_zero_argument(self):
        with self.assertRaises(TypeError):
            Rectangle()

    def test_one_argument(self):
        with self.assertRaises(TypeError):
            Rectangle(1)

    def test_width(self):
        '''Check for value of width'''
        num = Rectangle(5, 6, 7, 8, 13)
        self.assertEqual(5, num.width)

    def test_width_setter(self):
        '''Check getter function of width'''
        w = Rectangle(5, 2)
        w.width = 3
        self.assertEqual(3, w.width)

    def test_height(self):
        '''Check for value of height'''
        num = Rectangle(5, 6, 7, 8, 13)
        self.assertEqual(6, num.height)

    def test_height_setter(self):
        '''Check getter function of width'''
        h = Rectangle(5, 2)
        h.height = 33
        self.assertEqual(33, h.height)

    def test_x(self):
        '''Check for value of x'''
        num = Rectangle(5, 6, 7, 8, 13)
        self.assertEqual(7, num.x)

    def test_x_setter(self):
        '''Check getter function of width'''
        par1 = Rectangle(5, 2, 3)
        par1.x = 23
        self.assertEqual(23, par1.x)

    def test_y(self):
        '''Check for value of y'''
        num = Rectangle(5, 6, 7, 8, 13)
        self.assertEqual(8, num.y)

    def test_y_setter(self):
        '''Check getter function of width'''
        par2 = Rectangle(5, 2)
        par2.y = 31
        self.assertEqual(31, par2.y)

    def test_id(self):
        '''Check for value of id'''
        num = Rectangle(5, 6, 7, 8, 13)
        self.assertEqual(13, num.id)

    def test_id_setter(self):
        '''Check getter function of width'''
        par3 = Rectangle(5, 2)
        par3.id = 36
        self.assertEqual(36, par3.id)


if __name__ == '__main__':
    unittest.main()
