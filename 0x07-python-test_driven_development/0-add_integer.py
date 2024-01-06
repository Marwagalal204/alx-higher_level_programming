#!/usr/bin/python3
"""
add integers Modules
This module defines a function, add_integer(a, b=98), which adds two numbers.
"""


def add_integer(a, b=98):
    """a function that adds 2 integers."""
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    elif not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    a = int(a)
    b = int(b)
    return a + b
