import unittest
from models.base import Base
"""
This module for test cases for base base module
"""


class TestBase(unittest.TestCase):
    '''
    This class for test the Base calss
    '''
    def test_id_not_none(self):
        """NOT None id"""
        n = Base(77)
        self.assertEqual(77, n.id)

    def test_id_is_none(self):
        """id is None"""
        n = Base()
        self.assertEqual(1, n.id)

    def test_to_json_string(self):
        '''test json string representation'''
        dic = {'x': 2, 'width': 10, 'id': 1, 'height': 7, 'y': 8}
        inst = Base().to_json_string([dic])
        res = '[{"x": 2, "width": 10, "id": 1, "height": 7, "y": 8}]'
        self.assertEqual(inst, res)

    def test_to_json_string_more_dicts(self):
        '''test json string representation'''
        dic = [{'x': 2, 'width': 10, 'id': 1, 'height': 7, 'y': 8},
                {'x': 3, 'width': 22, 'id': 3, 'height': 17, 'y': 0}]
        inst = Base().to_json_string(dic)
        res = '[{"x": 2, "width": 10, "id": 1, "height": 7, "y": 8}, ' + \
        '{"x": 3, "width": 22, "id": 3, "height": 17, "y": 0}]'
        self.assertEqual(inst, res)

    def test_json_string_none(self):
        '''Check if json string is none'''
        inst = Base().to_json_string(None)
        self.assertEqual(inst, '[]')

    def test_json_string_empty(self):
        '''Check if json string is empty'''
        inst = Base().to_json_string({})
        self.assertEqual(inst, '[]')

if __name__ == '__main__':
    unittest.main()
