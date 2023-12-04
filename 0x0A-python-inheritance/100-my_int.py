#!/usr/bin/python3
"""A class MyInt that inherits from int"""


class MyInt(int):
    """Rebel version of an integer"""

    def __eq__(self, value):
        """Redefines equality operator to behave as inequality"""
        return self.real != value

    def __ne__(self, value):
        """Redefines the inequality operator to behave as equality"""
        return self.real == value
