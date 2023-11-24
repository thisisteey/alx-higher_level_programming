#!/usr/bin/python3
# function that adds 2 integers
"""An integer function that adds two integers, typecasting float
arguments to integers"""


def add_integer(a, b=98):
    """Adds and returns the integer addition of a and b
    Error to Raise:
    TypeError: for non-intger and non-float inputs for either a or b"""
    if ((not isinstance(a, int) and not isinstance(a, float))):
        raise TypeError("a must be an integer")
    if ((not isinstance(b, int) and not isinstance(b, float))):
        raise TypeError("b must be an integer")
    return (int(a) + int(b))
