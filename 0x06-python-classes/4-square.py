#!/usr/bin/python3
"""A class Square that defines a square by: (based on 3-square.py)"""


class Square:
    """Square Attributes: __size (int): the size of the square"""
    def __init(self, size=0):
        """Methods:
        __init__(self, size=0): intialises a new square with the
        specified size
        Args:
        size (int): size of the new square"""
        self.size = size

    def area(self):
        """calculates and returns the current area of the square"""
        return (self.__size) ** 2

    @property
    def size(self):
        """gets and returns the current size of the square"""
        return (self.__size)

    @size.setter
    def size(self,value):
        """sets the size attribute with the provided value after checking"""
        if type(value) is not int:
            raise TypeError("size must be an integer")
        else:
            if value < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = value
