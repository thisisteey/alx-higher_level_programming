#!/usr/bin/python3
"""A class Square that defines a square by: (based on 0-square.py)"""


class Square:
    """Square Attributes: __size (int); size of the square side"""
    def __init__(self, size):
        """Methods:
        __init__(self, size): initializes a new square instance with
        the specified size
            Args:
                size (int): Size of the new square"""
        self.__size = size
