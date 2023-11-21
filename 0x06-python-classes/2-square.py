#!/usr/bin/python3
"""A class Square that defines a square by: (based on 1-square.py)"""


class Square:
    """Square Attributes: __size (int): size of the square"""
    def __init__(self, size=0):
        """Methods:
    __init__(self, size=0): initializes a new square instance with
    the specified size.
    Args:
    size (int): the size of the new square. Default is 0
    Raises:
    TypeError: if the provided size is not an integer
    ValueError: if the provided size is less than 0"""
        if type(size) is int:
            if size < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = size
        else:
            raise TypeError("size must be an integer")
