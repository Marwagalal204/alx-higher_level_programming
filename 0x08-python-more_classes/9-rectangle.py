#!/usr/bin/python3
"""class rectangle"""


class Rectangle:
    """intialize privte attributes width and height"""
    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        self.__width = width
        self.__height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """getter function to retrive the value of width"""
        return self.__width

    """setter function to set the value of width"""
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
        """getter function to retrive the value of height"""
        return self.__height

    """setter function to set the value of width"""
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
        return ((self.__width + self.__height) * 2)

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

    def __repr__(self):
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        """Print a message for every deletion of a Rectangle."""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    def bigger_or_equal(rect_1, rect_2):
        """returns the rectangle with the greater area"""
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        elif not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")

        res1 = rect_1.area
        res2 = rect_2.area
        if res2 > res1:
            return rect_2
        else:
            return rect_1

    def square(cls, size=0):
        """returns a new Rectangle instance with width =height = size."""
