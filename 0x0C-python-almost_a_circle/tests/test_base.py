#!/usr/bin/python3
"""
Unit tests for the Base class

"""

import sys
import unittest
import inspect
import io
import pep8
from contextlib import redirect_stdout
from models.base import Base


class TestBase(unittest.TestCase):
    """
    Class for testing Base class' methods
    """

    @classmethod
    def setUpClass(cls):
        """
        Set up class method for the doc tests
        """
        cls.setup = inspect.getmembers(Base, inspect.isfunction)

    def test_class_docstring(self):
        """
        Tests if class docstring documentation exists
        """
        self.assertTrue(len(Base.__doc__) >= 1)

    def test_init_with_id(self):
        """
        Test if the __init__ method initializes with a given id
        """
        obj = Base(5)
        self.assertEqual(obj.id, 5)

    def test_init_without_id(self):
        """
        Test if the __init__ method initializes without a given id
        """
        obj = Base()
        self.assertEqual(obj.id, 1)

    def test_to_json_string_empty_list(self):
        """
        Test if to_json_string returns an empty list string
        """
        self.assertEqual(Base.to_json_string([]), "[]")

    def test_to_json_string_valid_list(self):
        """
        Test if to_json_string returns a valid JSON string
        """
        data = [{'id': 1, 'name': 'example'}, {'id': 2, 'name': 'test'}]
        result = Base.to_json_string(data)
        self.assertEqual(result, '[{"id": 1, "name": "example"}, {"id": 2, "name": "test"}]')

    def test_save_to_file_empty_list(self):
        """
        Test if save_to_file writes an empty list to the file
        """
        with open("Base.json", "w") as file:
            pass  # Clear the existing file content
        Base.save_to_file([])
        with open("Base.json", "r") as file:
            content = file.read()
            self.assertEqual(content, "[]")

    def test_from_json_string_empty_string(self):
        """
        Test if from_json_string returns an empty list for an empty string
        """
        self.assertEqual(Base.from_json_string(""), [])

    def test_from_json_string_valid_string(self):
        """
        Test if from_json_string returns a valid list from a JSON string
        """
        json_string = '[{"id": 1, "name": "example"}, {"id": 2, "name": "test"}]'
        result = Base.from_json_string(json_string)
        expected = [{'id': 1, 'name': 'example'}, {'id': 2, 'name': 'test'}]
        self.assertEqual(result, expected)

    def test_load_from_file_file_not_exist(self):
        """
        Test if load_from_file returns an empty list when the file doesn't exist
        """
        result = Base.load_from_file()
        self.assertEqual(result, [])
