#!/usr/bin/python3
"""Unittests for max_integer([..])."""

import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Define unittests for max_integer([..])."""

    def test_ordered_list(self):
        """Test an ordered list of integers."""
        ordered = [1, 2, 3, 4]
        self.assertEqual(max_integer(ordered), 4)

    def test_unordered_list(self):
        """Test an unordered list of integers."""
        unordered = [1, 2, 4, 9, 3, 5]
        self.assertEqual(max_integer(unordered), 9)

    def test_max_at_begginning(self):
        """Test a list with a beginning max value."""
        max_at_beginning = [9, 4, 3, 2, 1]
        self.assertEqual(max_integer(max_at_beginning), 9)

    def test_empty_list(self):
        """Test an empty list."""
        empty = []
        self.assertEqual(max_integer(empty), None)

    def test_one_element_list(self):
        """Test a list with a single element."""
        one_element = [7]
        self.assertEqual(max_integer(one_element), 7)

    def test_floats(self):
        """Test a list of floats."""
        floats = [2.5, 7.750, -9.123, 18.2, 6.0]
        self.assertEqual(max_integer(floats), 18.2)

    def test_ints_and_floats(self):
        """Test a list of ints and floats."""
        ints_and_floats = [1.53, 16.5, -9, 15, 6, 20]
        self.assertEqual(max_integer(ints_and_floats), 20)

    def test_string(self):
        """Test a string."""
        string = "Python is fun"
        self.assertEqual(max_integer(string), 'y')

    def test_list_of_strings(self):
        """Test a list of strings."""
        strings = ["Python", "is", "fun"]
        self.assertEqual(max_integer(strings), "is")

    def test_empty_string(self):
        """Test an empty string."""
        self.assertEqual(max_integer(""), None)

if __name__ == '__main__':
    unittest.main()