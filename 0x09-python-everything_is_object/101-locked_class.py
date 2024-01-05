#!/usr/bin/python3
"""Class LockedClass"""


class LockedClass:
    """Class LockedClass"""
    def __setattr__(self, name, value):
        if name != 'first_name':
            msg = f"'LockedClass' object has no attribute '{name}'"
            raise AttributeError(msg)
        super().__setattr__(name, value)
