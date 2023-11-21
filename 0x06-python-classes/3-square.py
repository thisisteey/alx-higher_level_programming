#!/usr/bin/python3
"""A class Square that defines a square by: (based on 2-square.py)"""


class Square:
    """Square Attributes: __size (int): the size of the square"""
    def __init__(self, size=0):
        """Methods:
            __init__(self, size=0): initializes a new square with
            specified size
            Args:
                size (int): size of the nw square which is default 0
            Raises:
                TypeError: if the provided size is not an integer
                ValueError: if the provided size is less than 0"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """area(self):
            calculates and return the current area of the square"""
        return (self.__size * self.__size)
