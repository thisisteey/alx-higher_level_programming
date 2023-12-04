#!/usr/bin/python3
"""A class Rectangle that inherits from BaseGeometry (7-base_geometry.py)"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Representing a rectangle using BaseGeometry"""

    def __init__(self, width, height):
        """Initializes the rectangle
        Args:
        width (int): the width of the rectangle
        height (int): the height of the rectangle"""
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
