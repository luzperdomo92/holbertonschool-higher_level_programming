#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """Unit test for max_integer([..])"""

    def test_filled_list(self):
        """Test max value for filled_list"""
        data = [1, 2, 7, 4]
        result = max_integer(data)
        self.assertEqual(result, 7)
    
    def test_negative_list(self):
        """Test max value for negative_list"""
        data = [1, 2, -7, -4]
        result = max_integer(data)
        self.assertEqual(result, 2)
    
    def test_default_list(self):
        """Test max value for default_list"""
        result = max_integer()
        self.assertEqual(result, None)

    def test_empty_list(self):
        """Test max value for empty_list"""
        data = []
        result = max_integer(data)
        self.assertEqual(result, None)

    def test_string(self):
        """Test max value for string"""
        data = "tacoxlocos"
        result = max_integer(data)
        self.assertEqual(result, 'x')

    def test_empty_string(self):
        """Test max value for empty_string"""
        data = ""
        result = max_integer(data)
        self.assertEqual(result, None)
    
    def test_alpha_list(self):
        """Test max value for alpha_list"""
        data = [1, 'a', 40, -100, 'z', 'A']
        with self.assertRaises(TypeError):
            max_integer(data)
    
    def test_boolean(self):
        """Test max value for boolean"""
        with self.assertRaises(TypeError):
            max_integer(True)

    def test_boolean_list(self):
        """Test max value for boolean_list"""
        data = [True, False, False, True]
        result = max_integer(data)
        self.assertEqual(result, True)

    def test_string_list(self):
        """Test max value for string_list"""
        data = ['t', 'a', 'x', 'c', 'o']
        result = max_integer(data)
        self.assertEqual(result, 'x')

    def test_string_mayus_list(self):
        """Test max value for string_mayus_list"""
        data = ['t', 'a', 'x', 'C', 'o']
        result = max_integer(data)
        self.assertEqual(result, 'x')

    def test_none(self):
        """Test max value for none"""
        with self.assertRaises(TypeError):
            max_integer(None)

if __name__ == '__main__':
    unittest.main()
