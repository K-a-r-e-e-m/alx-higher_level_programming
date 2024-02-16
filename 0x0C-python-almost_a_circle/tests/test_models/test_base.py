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

if __name__ == '__main__':
    unittest.main()
