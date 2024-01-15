#!/usr/bin/python3

"""
unittest for square class
"""
import unittest
from models.square import Square


class TestSquare(unittest.TestCase):

    def setUp(self):
        # Initialize common variables or perform any setup needed for tests
        pass

    def tearDown(self):
        # Clean up after the test methods run
        pass

    def test_constructor(self):
        # Test the constructor
        square = Square(5, 2, 3, 1)
        self.assertEqual(square.size, 5)
        self.assertEqual(square.width, 5)
        self.assertEqual(square.height, 5)
        self.assertEqual(square.x, 2)
        self.assertEqual(square.y, 3)
        self.assertEqual(square.id, 1)

    def test_size_setter(self):
        # Test the size setter
        square = Square(5)
        square.size = 10
        self.assertEqual(square.size, 10)
        self.assertEqual(square.width, 10)
        self.assertEqual(square.height, 10)

        with self.assertRaises(TypeError):
            square.size = "string"

        with self.assertRaises(ValueError):
            square.size = 0

    # Add similar tests for x, y, and their setters

    def test_update(self):
        # Test the update method
        square = Square(5, 2, 3, 1)
        square.update(2, 8, 4, 5)
        self.assertEqual(square.id, 2)
        self.assertEqual(square.size, 8)
        self.assertEqual(square.x, 4)
        self.assertEqual(square.y, 5)

        square.update(size=15, y=7)
        self.assertEqual(square.size, 15)
        self.assertEqual(square.y, 7)

    def test_to_dictionary(self):
        # Test the to_dictionary method
        square = Square(5, 2, 3, 1)
        expected_dict = {'id': 1, 'size': 5, 'x': 2, 'y': 3}
        self.assertEqual(square.to_dictionary(), expected_dict)

    def test_str(self):
        # Test the __str__ method
        square = Square(5, 2, 3, 1)
        expected_str = '[Square] (1) 2/3 - 5'
        self.assertEqual(str(square), expected_str)


if __name__ == '__main__':
    unittest.main()
