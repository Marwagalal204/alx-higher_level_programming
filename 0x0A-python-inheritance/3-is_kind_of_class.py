#!/usr/bin/python3
"""Defines a class-checking function."""


def is_kind_of_class(obj, a_class):
    """Check if an object is exactly an instance of a given class."""
    if type(obj) is a_class or isinstance(obj, a_class):
        return True
    else:
        return False
