#!/usr/bin/python3
# function that prints a square with the character #
"""A function that prints a square the '#' charcater"""


def print_square(size):
    """Args:
    size (int): the height and width of the square
    Error to Raise:
    TypeError: 1. if the size is not an integer
                2. if the size is a float and less than 0
    ValueError: if the size is less than 0"""
    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if type(size) is float and size < 0:
        raise TypeError("size must be an integer")
    for x in range(size):
        [print("#", end="") for y in range(size)]
        print("")
