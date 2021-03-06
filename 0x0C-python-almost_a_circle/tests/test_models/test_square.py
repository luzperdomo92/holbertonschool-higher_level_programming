#!/usr/bin/python3
""" Unittest for class Square """
import unittest
import sys
import io
import json
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestSquare(unittest.TestCase):
    """tests for class Square and its methods
    """
    def setUp(self):
        """setUp for each test method"""
        self.a = Square(2)  # id is 1
        self.b = Square(3, 1, 2, 100)  # id is 100
        self.c = Square(5, 0, 0, None)  # id is 2

    def tearDown(self):
        """Reset counter to 0 for each test method"""
        Base._Base__nb_objects = 0

    def test_inheritance(self):
        """test for inheritance"""
        self.assertIsInstance(self.a, Base)
        self.assertIsInstance(self.a, Rectangle)
        self.assertIsInstance(self.a, Square)

    def test_not_inheritance(self):
        """test for not inheritance"""
        self.assertNotIsInstance(Base, Square)
        self.assertNotIsInstance(Rectangle, Square)

    def test_id(self):
        """test for id"""
        self.assertEqual(self.a.id, 1)
        self.assertEqual(self.b.id, 100)
        self.assertEqual(self.c.id, 2)
        self.c.id = 98
        self.assertEqual(self.c.id, 98)

    def test_size(self):
        """test for size"""
        self.assertEqual(self.a.height, 2)
        self.assertEqual(self.a.width, 2)
        self.assertEqual(self.b.height, 3)
        self.assertEqual(self.b.width, 3)
        self.assertEqual(self.c.height, 5)
        self.assertEqual(self.c.width, 5)
        self.c.size = 10
        self.assertEqual(self.c.width, 10)

        self.assertRaises(TypeError, self.c.size, "hi")
        self.assertRaises(TypeError, self.c.size, [1, 2])
        self.assertRaises(TypeError, self.c.size, {"hi": 0})
        with self.assertRaises(ValueError):
            self.c.size = -1
        with self.assertRaises(ValueError):
            self.c.size = 0

    def test_x(self):
        """test for x"""
        self.assertEqual(self.a.x, 0)
        self.assertEqual(self.b.x, 1)
        self.assertEqual(self.c.x, 0)
        self.c.x = 98
        self.assertEqual(self.c.x, 98)
        self.assertRaises(TypeError, self.c.x, "hi")
        with self.assertRaises(ValueError):
            self.c.x = -1

    def test_y(self):
        """test for y"""
        self.assertEqual(self.a.y, 0)
        self.assertEqual(self.b.y, 2)
        self.assertEqual(self.c.y, 0)
        self.c.y = 96
        self.assertEqual(self.c.y, 96)
        self.assertRaises(TypeError, self.c.y, "hi")
        with self.assertRaises(ValueError):
            self.c.y = -1

    def test_exceptions(self):
        self.assertRaises(TypeError, Square, "1")
        self.assertRaises(TypeError, Square, 1, "2")
        self.assertRaises(TypeError, Square, 1, 2, "3")
        self.assertRaises(ValueError, Square, 0)
        self.assertRaises(ValueError, Square, -1)
        self.assertRaises(ValueError, Square, 1, -2)
        self.assertRaises(ValueError, Square, 1, 2, -3)

    def test_str_method(self):
        """test for str method"""
        expected = "[Square] (1) 0/0 - 2\n"
        output = io.StringIO()
        sys.stdout = output
        print(self.a)
        self.assertEqual(expected, output.getvalue())

        expected = "[Square] (100) 1/2 - 3\n"
        output = io.StringIO()
        sys.stdout = output
        print(self.b)
        self.assertEqual(expected, output.getvalue())

        expected = "[Square] (2) 0/0 - 5\n"
        output = io.StringIO()
        sys.stdout = output
        print(self.c)
        self.assertEqual(expected, output.getvalue())

    def test_square_update(self):
        """test for square method update"""
        self.a.update(10)
        expected = "[Square] (10) 0/0 - 2\n"
        output = io.StringIO()
        sys.stdout = output
        print(self.a)
        self.assertEqual(expected, output.getvalue())

        self.a.update(1, 3)
        expected = "[Square] (1) 0/0 - 3\n"
        output = io.StringIO()
        sys.stdout = output
        print(self.a)
        self.assertEqual(expected, output.getvalue())

        self.a.update(1, 2, 3)
        expected = "[Square] (1) 3/0 - 2\n"
        output = io.StringIO()
        sys.stdout = output
        print(self.a)
        self.assertEqual(expected, output.getvalue())

        self.a.update(1, 2, 3, 4)
        expected = "[Square] (1) 3/4 - 2\n"
        output = io.StringIO()
        sys.stdout = output
        print(self.a)
        self.assertEqual(expected, output.getvalue())

        self.a.update(x=12)
        expected = "[Square] (1) 12/4 - 2\n"
        output = io.StringIO()
        sys.stdout = output
        print(self.a)
        self.assertEqual(expected, output.getvalue())

        self.a.update(size=7, id=89, y=1)
        expected = "[Square] (89) 12/1 - 7\n"
        output = io.StringIO()
        sys.stdout = output
        print(self.a)
        self.assertEqual(expected, output.getvalue())

    def test_to_dictionary(self):
        a_dict = self.a.to_dictionary()
        expected = {"size": 2, "x": 0, "y": 0, "id": 1}
        self.assertDictEqual(a_dict, expected)

    def test_save_to_file(self):
        Square.save_to_file([self.a, self.b])
        with open("Square.json", "r", encoding="utf8") as f:
            json_list = f.read()
        list_of_dicts = json.loads(json_list)
        self.assertDictEqual(list_of_dicts[0], self.a.to_dictionary())
        self.assertDictEqual(list_of_dicts[1], self.b.to_dictionary())

        Square.save_to_file(None)
        with open("Square.json", "r", encoding="utf8") as f:
            json_list = f.read()
        empty_list = json.loads(json_list)
        self.assertEqual(empty_list, [])

        Square.save_to_file([])
        with open("Square.json", "r", encoding="utf8") as f:
            json_list = f.read()
        empty_list = json.loads(json_list)
        self.assertEqual(empty_list, [])

    def test_create(self):
        a_dict = self.a.to_dictionary()
        square = Square.create(**a_dict)
        self.assertDictEqual(a_dict, square.to_dictionary())

        a_dict = {'id': 98}
        expected = {'id': 98, 'size': 1, 'x': 0, 'y': 0}
        square = Square.create(**a_dict)
        self.assertDictEqual(expected, square.to_dictionary())

        a_dict = {'id': 98, 'size': 2}
        expected = {'id': 98, 'size': 2, 'x': 0, 'y': 0}
        square = Square.create(**a_dict)
        self.assertDictEqual(expected, square.to_dictionary())

        a_dict = {'id': 98, 'size': 2, 'x': 1}
        expected = {'id': 98, 'size': 2, 'x': 1, 'y': 0}
        square = Square.create(**a_dict)
        self.assertDictEqual(expected, square.to_dictionary())

    def test_load_from_file(self):
        empty_list = Square.load_from_file()
        self.assertEqual([], empty_list)

        Square.save_to_file([self.a])
        list_of_sqs = Square.load_from_file()
        self.assertDictEqual(list_of_sqs[0].to_dictionary(),
                             self.a.to_dictionary())


if '__name__' == '__main__':
    unittest.main()
