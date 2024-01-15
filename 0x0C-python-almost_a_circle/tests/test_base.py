#!/usr/bin/python3
"""
Unit tests for the Base class
"""
import unittest
import os
from models.base import Base


class TestBase(unittest.TestCase):

    def setUp(self):
        # Initialize common variables or perform any setup needed for tests
        pass

    def tearDown(self):
        # Clean up after the test methods run
        try:
            os.remove("Base.json")
        except FileNotFoundError:
            pass

    def test_constructor(self):
        # Test the constructor
        obj = Base(1)
        self.assertEqual(obj.id, 1)

    def test_to_json_string(self):
        # Test the to_json_string method
        obj_list = [{'id': 1, 'name': 'Alice'}, {'id': 2, 'name': 'Bob'}]
        json_string = Base.to_json_string(obj_list)
        self.assertEqual(json_string, '[{"id": 1, "name": "Alice"}'
                         ', {"id": 2, "name": "Bob"}]')

        empty_list = []
        empty_json = Base.to_json_string(empty_list)
        self.assertEqual(empty_json, '[]')

    def test_save_to_file(self):
        # Test the save_to_file method
        obj_list = [{'id': 1, 'name': 'Alice'}, {'id': 2, 'name': 'Bob'}]
        Base.save_to_file(obj_list)
        with open("Base.json", "r") as jsonfile:
            self.assertEqual(jsonfile.read(), '[{"id": 1, "name": "Alice"},'
                             '{"id": 2, "name": "Bob"}]')

        empty_list = []
        Base.save_to_file(empty_list)
        with open("Base.json", "r") as jsonfile:
            self.assertEqual(jsonfile.read(), '[]')

    def test_from_json_string(self):
        # Test the from_json_string method
        json_string = '[{"id": 1, "name": "Alice"}, {"id": 2, "name": "Bob"}]'
        obj_list = Base.from_json_string(json_string)
        self.assertEqual(obj_list, [{'id': 1, 'name': 'Alice'},
                                    {'id': 2, 'name': 'Bob'}])

        empty_json = '[]'
        empty_list = Base.from_json_string(empty_json)
        self.assertEqual(empty_list, [])

    def test_create(self):
        # Test the create method
        obj_dict = {'id': 1, 'name': 'Alice'}
        obj = Base.create(**obj_dict)
        self.assertEqual(obj.id, 1)
        self.assertEqual(obj.name, 'Alice')

    def test_load_from_file(self):
        # Test the load_from_file method
        obj_list = [{'id': 1, 'name': 'Alice'}, {'id': 2, 'name': 'Bob'}]
        Base.save_to_file(obj_list)

        loaded_objs = Base.load_from_file()
        self.assertEqual(len(loaded_objs), 2)
        self.assertEqual(loaded_objs[0].id, 1)
        self.assertEqual(loaded_objs[1].id, 2)

        # Test with an empty file
        empty_list = []
        Base.save_to_file(empty_list)
        loaded_empty_objs = Base.load_from_file()
        self.assertEqual(len(loaded_empty_objs), 0)


if __name__ == '__main__':
    unittest.main()
