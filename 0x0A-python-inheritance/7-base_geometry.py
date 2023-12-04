#!/usr/bin/python3
"""A class BaseGeometry (based on 6-base_geometry.py)"""


class BaseGeometry:
    """Representing the defined basegeometry"""

    def area(self):
        """An area of a basegeometry that is not implemented"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Checks and validates a parameter as an integer
        Args:
        name (str): The name of the parameter
        value (int): the parameter to be validated"""
        if type(value) != int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
