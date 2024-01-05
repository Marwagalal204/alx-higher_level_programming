#!/usr/bin/python3
"""class rectangle"""


class Rectangle:
    """intialize privte attributes width and height"""
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        """getter/setter function to retrive the value of width"""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
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
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        """instance  to find the area of a rectanle"""
        return self.__width * self.__height

    def perimeter(self):
        if self.__width == 0 or self.__height == 0:
            return (0)
        """instance  to find the area of a perimeter"""
        return ((self.__width * 2) + (self.__height * 2))

    def __str__(self):
        """method prints the rectangle with the # character"""
        result = ""
        if self.__width == 0 or self.__height == 0:
            return (0)
        else:
            for i in range(self.__height):
                for j in range(self.__width):
                    result += '#'
                if i < self.__height - 1:
                    result += '\n'
        return result
