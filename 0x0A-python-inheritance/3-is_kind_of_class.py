#!/usr/bin/python3
"""Defines a function checking if an object is an instance
or inherits from a specified class"""


def is_kind_of_class(obj, a_class):
    """Checks and returns True if an object is an instance of a class
    Args:
    obj (any): the object that will be checked
    a_class (type): the class to match if the obj is of the same type"""
    if isinstance(obj, a_class):
        return True
    else:
        return False
