#!/usr/bin/python3
"""managing id attributes"""
import json
import csv
import turtle
import os


class Base:
    """class base"""

    __nb_objects = 0

    def __init__(self, id=None):
        """intializing method"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """static method convert from python to Jason"""
        x = json.dumps(list_dictionaries)

        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        return x

    @classmethod
    def save_to_file(cls, list_objs):
        """class metod saves the converted data"""
        filename = cls.__name__ + ".json"
        json_string = cls.to_json_string(list_objs) if list_objs else "[]"

        with open(filename, 'w') as jsonfile:
            jsonfile.write(json_string)

    @staticmethod
    def from_json_string(json_string):
        """static method convert from jason to python"""

        if json_string is None or json_string == "":
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """class method create"""
        if dictionary and dictionary != {}:
            if cls.__name__ == "Rectangle":
                new = cls(1, 1)
            else:
                new = cls(1)
            new.update(**dictionary)
            return new

    @classmethod
    def load_from_file(cls):
        """class method load_from_file"""
        filename = str(cls.__name__) + ".json"
        try:
            with open(filename, "r") as jsonfile:
                list_dicts = Base.from_json_string(jsonfile.read())
                return [cls.create(**d) for d in list_dicts]
        except IOError:
            return []
