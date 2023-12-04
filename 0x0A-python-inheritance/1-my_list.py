#!/usr/bin/python3
"""A class MyList that inherits from list"""


class MyList(list):
    """Implements printing sorted list of the builtin list class"""

    def print_sorted(self):
        """Prints the list from the class in sorted ascending order"""
        print(sorted(self))
