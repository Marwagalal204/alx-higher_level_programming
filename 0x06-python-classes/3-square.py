#!/usr/bin/python3
"""Defines a class Square."""


class Square:
    """Represents a square with a private instance attribute size."""
    def __init__(self, size=0):
        """Instantiates the Square with an optional size."""
        self.__size = size
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        """Calculates and returns the area of the square."""
        return self.__size ** 2
