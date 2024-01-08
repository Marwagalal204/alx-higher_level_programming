#!/usr/bin/python3
"""MyList Class"""


class MyList(list):
    """list subclass"""
    def __init__(self):
        """initializes the object"""
        super().__init__()

    def print_sorted(self):
        """print sorted list"""
        sortedlist = sorted(self)
        print(sortedlist)
