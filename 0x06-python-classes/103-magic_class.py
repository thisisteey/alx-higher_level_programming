#!/usr/bin/python3
"""A MagicClass that does exactly the same as a python bytecode provided"""
from math import pi


class MagicClass:
    """A geometric circle is represented"""
    def __init__(self, radius=0):
        """initializes the magicclass
        Args:
        radius(float or int): radiu of the new MagicClass"""
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError("radius must be a number")
        self.__radius = radius

    def area(self):
        """gets and returns the area of the magicclass"""
        return (self.__radius ** 2 * pi)

    def circumference(self):
        """gets and return the circumference of the magicclass"""
        return (2 * pi * self.__radius)
