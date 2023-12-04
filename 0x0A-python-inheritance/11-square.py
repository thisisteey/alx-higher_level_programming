#!/usr/bin/python3
"""A class Square that inherits from Rectangle (9-rectangle.py)
(task based on 10-square.py)."""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Representing a square using rectangle"""

    def __init__(self, size):
        """initializes the square
        Args:
        size (int): the size of the square"""
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """Calculates the area of the square"""
        return self.__size ** 2

    def __str__(self):
        """informal representation of the square string"""
        return (f"[Square] {self.__size}/{self.__size}")
