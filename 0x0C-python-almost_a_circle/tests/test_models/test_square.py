#!/usr/bin/python3
"""This module tests the Square class in square module"""
import unittest
from models.square import Square
from models.base import Base
from io import StringIO
import sys
import os.path


class TestRectangle(unittest.TestCase):
    '''In this class I will provide some testcases to test the Square'''
    def test_inheritance(self):
        '''Check for inheritance of class'''
        self.assertIsInstance(Square(2, 5), Base)

    def test_zero_argument(self):
        '''If there is no arguments passed'''
        with self.assertRaises(TypeError):
            Square()

    def test_one_argument(self):
        '''If pass one arguemnt'''
        num = Square(1)
        self.assertEqual(num.width, 1)
        self.assertEqual(num.height, 1)

    def test_two_arguments(self):
        '''Check for two arguments'''
        num = Square(1, 2)
        self.assertEqual(num.size, 1)
        self.assertEqual(num.x, 2)

    def test_three_arguments(self):
        '''Check for three arguments'''
        num = Square(1, 2, 3)
        self.assertEqual(num.size, 1)
        self.assertEqual(num.x, 2)
        self.assertEqual(num.y, 3)

    def test_four_arguments(self):
        '''Check for four arguments'''
        num = Square(1, 2, 3, 4)
        self.assertEqual(num.size, 1)
        self.assertEqual(num.x, 2)
        self.assertEqual(num.y, 3)
        self.assertEqual(num.id, 4)

    def test_size(self):
        '''Check for value of size'''
        num = Square(5, 6, 7, 8)
        self.assertEqual(5, num.size)

    def test_size_setter(self):
        '''Check getter function of size'''
        w = Square(5)
        w.size = 3
        self.assertEqual(3, w.size)

    def test_size_string(self):
        '''Check if size is not integar'''
        with self.assertRaises(TypeError):
            Square('df')

    def test_size_negative(self):
        '''Check if size is negative'''
        with self.assertRaises(ValueError):
            Square(-6)

    def test_size_zero(self):
        '''Check if size is zero'''
        with self.assertRaises(ValueError):
            Square(0)

    def test_x(self):
        '''Check for value of x'''
        num = Square(5, 6, 7, 8)
        self.assertEqual(6, num.x)

    def test_x_setter(self):
        '''Check getter function of width'''
        par1 = Square(5, 2, 3)
        par1.x = 23
        self.assertEqual(23, par1.x)

    def test_x_string(self):
        '''Check if x is not integar'''
        with self.assertRaises(TypeError):
            Square(3, '3')

    def test_x_negative(self):
        '''Check if height is negative'''
        with self.assertRaises(ValueError):
            Square(6, -2)

    def test_y(self):
        '''Check for value of y'''
        num = Square(5, 6, 7)
        self.assertEqual(7, num.y)

    def test_y_setter(self):
        '''Check getter function of width'''
        par2 = Square(5, 2)
        par2.y = 31
        self.assertEqual(31, par2.y)

    def test_y_string(self):
        '''Check if y is not integar'''
        with self.assertRaises(TypeError):
            Square(3, 2, '88')

    def test_y_negative(self):
        '''Check if y is negative'''
        with self.assertRaises(ValueError):
            Square(6, 2, -2)

    def test_id(self):
        '''Check for value of id'''
        num = Square(5, 6, 7, 8)
        self.assertEqual(8, num.id)

    def test_id_setter(self):
        '''Check getter function of width'''
        par3 = Square(5, 2)
        par3.id = 36
        self.assertEqual(36, par3.id)

    def test_area(self):
        '''Test area or Square'''
        inst = Square(2)
        self.assertEqual(inst.area(), 4)

    def test__str__(self):
        '''Test string representation'''
        inst = Square(2)
        out = f'[Square] ({inst.id}) 0/0 - 2'
        self.assertEqual(str(inst), out)

    def test__str__x(self):
        '''Test string representation'''
        inst = Square(2, 5)
        out = f'[Square] ({inst.id}) 5/0 - 2'
        self.assertEqual(str(inst), out)

    def test__str__xy(self):
        '''Test string representation'''
        inst = Square(2, 5, 8)
        out = f'[Square] ({inst.id}) 5/8 - 2'
        self.assertEqual(str(inst), out)

    def test__str__xy_id(self):
        '''Test string representation'''
        inst = Square(2, 5, 8, 22)
        out = '[Square] (22) 5/8 - 2'
        self.assertEqual(str(inst), out)

    def test_update_args_id(self):
        '''Test the update on instance's attributes'''
        inst = Square(2, 4, 5)
        inst.update(1000)
        self.assertEqual(inst.id, 1000)
        self.assertEqual(inst.size, 2)
        self.assertEqual(inst.x, 4)
        self.assertEqual(inst.y, 5)

    def test_update_args_id_width(self):
        '''Test the update on instance's attributes'''
        inst = Square(2, 3, 4, 5)
        inst.update(12, 223, 4, 5)
        self.assertEqual(inst.id, 12)
        self.assertEqual(inst.size, 223)
        self.assertEqual(inst.x, 4)
        self.assertEqual(inst.y, 5)

    def test_update_args_all(self):
        '''Test the update on instance's attributes'''
        inst = Square(2, 3, 4, 5)
        inst.update(12, 223, 47, 532)
        self.assertEqual(inst.id, 12)
        self.assertEqual(inst.size, 223)
        self.assertEqual(inst.x, 47)
        self.assertEqual(inst.y, 532)

    def test_update_args_id_kwargs(self):
        '''Test the update on instance's attributes'''
        inst = Square(2, 4, 5, 7)
        inst.update(id=22)
        self.assertEqual(str(inst), '[Square] (22) 4/5 - 2')

    def test_update_args_id_width_kwargs(self):
        '''Test the update on instance's attributes'''
        inst = Square(2, 4, 5, 7)
        inst.update(id=22, size=8)
        self.assertEqual(str(inst), '[Square] (22) 4/5 - 8')

    def test_update_args_id_width_height_x(self):
        '''Test the update on instance's attributes'''
        inst = Square(2, 3, 5, 7)
        inst.update(id=22, size=8, x=3)
        self.assertEqual(str(inst), '[Square] (22) 3/5 - 8')
        
    def test_update_args_id_width_height_xy(self):
        '''Test the update on instance's attributes'''
        inst = Square(2, 3, 5, 7)
        inst.update(id=22, size=8, height=12, x=3, y=1)
        self.assertEqual(str(inst), '[Square] (22) 3/1 - 8')

    def test_to_dictionary(self):
        '''Test convertion to dictionary'''
        inst = Square(2, 4, 5, 7)
        outp = inst.to_dictionary()
        self.assertEqual(outp, {'id': 7, 'size': 2, 'x': 4, 'y': 5})

    def test_create_id(self):
        '''Test create function'''
        inst = Square(2)
        out = inst.create(**{'id': 7})
        self.assertEqual(str(out), '[Square] (7) 0/0 - 1')

    def test_create_id_width(self):
        '''Test create function'''
        out = Square.create(**{'id': 7, 'size': 2})
        self.assertEqual(str(out), '[Square] (7) 0/0 - 2')

    def test_create_x(self):
        '''Test create function'''
        out = Square.create(**{'id': 7, 'size': 3, 'x': 4})
        self.assertEqual(str(out), '[Square] (7) 4/0 - 3')

    def test_create_x_y(self):
        '''Test create function'''
        out = Square.create(**{'id': 7, 'size': 3, 'x': 4, 'y': 5})
        self.assertEqual(str(out), '[Square] (7) 4/5 - 3')
        
class TestSquareOutputDisplay(unittest.TestCase):
    '''This class for test display method'''
    def capture_output(self, inst, *args):
        '''Capture the output of screeen from stdout'''
        # Create StringIO object to capture output temporary 
        # instead of __stdout__ (the output on screen or terminal)
    
        # create an object to store the output like a file but in memory not disk
        output = StringIO() 
        # Move the standerd output from Screen or teminal 
        # to this buffer (A temporary storage area in memory)
        sys.stdout = output
        # Call method that print, the output will display on the StringIo not screen!
        if args:
            print(inst)
        else:
            inst.display()
        # Restore the output to standered output __stdout__
        sys.stdout = sys.__stdout__
        # Get the value of these data that stored in memeory 
        return output.getvalue()

    def test_display(self):
        '''Test display method without x and y'''
        inst = Square(2)
        output = self.capture_output(inst)
        self.assertEqual(output, '##\n##\n')

    def test_display_x0_y0(self):
        '''Test display method without x and y'''
        inst = Square(1, 0, 0)
        output = self.capture_output(inst)
        self.assertEqual(output, '#\n')

    def test_display_x(self):
        '''Test display method without x and y'''
        inst = Square(2, 2)
        output = self.capture_output(inst)
        self.assertEqual(output, '  ##\n  ##\n')

    def test_display_y(self):
        '''Test display method without x and y'''
        inst = Square(2, 0, 3)
        output = self.capture_output(inst)
        self.assertEqual(output, '\n\n\n##\n##\n')

    def test_display_xy_(self):
        '''Test display method without x and y'''
        inst = Square(2, 1, 2)
        output = self.capture_output(inst)
        self.assertEqual(output, '\n\n ##\n ##\n')

    def test__str__with_print(self):
        '''Test string representation'''
        inst = Square(2)
        output = self.capture_output(inst, True)
        out = f'[Square] ({inst.id}) 0/0 - {inst.size}\n'
        self.assertEqual(output, out)

class TestFileSaveAndLoad(unittest.TestCase):
    '''This file to test save and load file'''

    def setUp(self):
        '''Set up temporary files for tests'''
        self.filename = 'Square.json'

    def tearDown(self):
        '''Clean up files after tests'''
        try:
            os.remove(self.filename)
        except FileNotFoundError:
            pass

    def test_save_to_file_None(self):
        '''test save to file module'''
        out = Square.save_to_file(None)
        with open('Square.json', 'r') as data:
            out = data.read()
        self.assertEqual(out, '[]')

    def test_save_to_file_Empty(self):
        '''test save to file module'''
        out = Square.save_to_file([])
        with open('Square.json', 'r') as data:
            out = data.read()
        self.assertEqual(out, '[]')
        
    def test_save_to_file(self):
        '''test save to file module'''
        r1 = Square(10, 7, 2, 8)
        r2 = Square(2, 4)
        out = Square.save_to_file([r1, r2])
        with open('Square.json', 'r') as data:
            out = data.read()
        self.assertEqual(out, Square.to_json_string([r1.to_dictionary(), r2.to_dictionary()]))

    def test_load_from_file_not_exists(self):
        '''Test load from json file method'''
        inst = Square.load_from_file()
        self.assertEqual(inst, [])

    def test_load_from_file_exists(self):
        '''Test load from json file method'''
        r1 = Square(10, 7, 2, 8)
        list_rectangles_input = [r1]
        Square.save_to_file(list_rectangles_input)
        list_rectangles_output = Square.load_from_file()
        self.assertEqual(r1.id, list_rectangles_output[0].id)

if __name__ == '__main__':
    unittest.main()
