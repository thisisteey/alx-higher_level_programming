#!/usr/bin/python3
"""A function that returns True if the object is exactly an
instance of the specified class ; otherwise False"""


def is_same_class(obj, a_class):
    """Checks and returns True if an object is an instance of a class
    Args:
    obj (any): the object that will be checked
    a_class (type): the class to match if the obj is of the same type"""
    if type(obj) == a_class:
        return True
    else:
        return False
