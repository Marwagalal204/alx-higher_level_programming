#!/usr/bin/python3
"""a function that prints a square using #"""


def print_square(size):
    """print size square"""
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        print("#" * size)
