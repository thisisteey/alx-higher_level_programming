#!/usr/bin/python3
"""A class Square that defines a square by: (based on 3-square.py)"""


class Square:
    """A square class represented"""
    def __init__(self, size=0):
        """Initialize the square class
        Args:
        size (int): size of the square"""
        self.size = size

    @property
    def size(self):
        """gets and returns the current size of the square"""
        return (self.__size)

    @size.setter
    def size(self, value):
        """sets the square size"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """calculates and returns the current area of the square"""
        return (self.__size * self.__size)
