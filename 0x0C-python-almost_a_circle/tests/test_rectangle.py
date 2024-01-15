#!/usr/bin/python3

"""
unittest for rectangle class
"""

import sys
import unittest
import io
from models.rectangle import Rectangle


class test_Rectangle(unittest.TestCase):
    """Testing rectangle class methods"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_constructor(self):
        rect = Rectangle(5, 10, 2, 3, 1)
        self.assertEqual(rect.width, 5)
        self.assertEqual(rect.height, 10)
        self.assertEqual(rect.x, 2)
        self.assertEqual(rect.y, 3)
        self.assertEqual(rect.id, 1)

    def test_width_setter(self):
        rect = Rectangle(5, 10)
        rect.width = 15
        self.assertEqual(rect.width, 15)

        with self.assertRaises(TypeError):
            rect.width = "string"

        with self.assertRaises(ValueError):
            rect.width = 0

    def test_area(self):
        rect = Rectangle(5, 10)
        self.assertEqual(rect.area(), 50)

    def test_display(self):
        pass

    def test_str(self):
        rect = Rectangle(5, 10, 2, 3, 1)
        expected_str = '[Rectangle] (1) 2/3 - 5/10'
        self.assertEqual(str(rect), expected_str)

    def test_update(self):
        rect = Rectangle(5, 10, 2, 3, 1)
        rect.update(2, 8, 12, 4, 5)
        self.assertEqual(rect.id, 2)
        self.assertEqual(rect.width, 8)
        self.assertEqual(rect.height, 12)
        self.assertEqual(rect.x, 4)
        self.assertEqual(rect.y, 5)

        rect.update(width=15, y=7)
        self.assertEqual(rect.width, 15)
        self.assertEqual(rect.y, 7)

    def test_to_dictionary(self):
        rect = Rectangle(5, 10, 2, 3, 1)
        expected_dict = {'id': 1, 'width': 5, 'height': 10, 'x': 2, 'y': 3}
        self.assertEqual(rect.to_dictionary(), expected_dict)


if __name__ == '__main__':
    unittest.main()
