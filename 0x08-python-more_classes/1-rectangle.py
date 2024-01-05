#!/usr/bin/python3
"""class rectangle"""


class Rectangle:
    """intialize privte attributes width and height"""
    def __init__(self, width=0, height=0):
        self.__width = width
        self.__height = height

        if type(width) is int:
            raise TypeError("width must be an integer")
        elif type(height) is int:
            raise TypeError("height must be an integer")
        elif width < 0:
            raise ValueError("width must be >= 0")
        elif height < 0:
            raise ValueError("height must be >= 0")

    @property
    def width(self):
        """getter/setter function to retrive the value of width"""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(int, value):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """getter/setter function to retrive the value of height"""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(int, value):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value
