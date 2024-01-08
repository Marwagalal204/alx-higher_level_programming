#!/usr/bin/python3
"""MyList Class"""


class MyList(list):
    """list subclass"""

    def print_sorted(self):
        """print sorted list"""
        sortedlist = sorted(self)
        print(sortedlist)
