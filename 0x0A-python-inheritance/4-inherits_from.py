#!/usr/bin/python3
"""Defines a function checking if an object is an instace of
a class inheriting from the specified class"""


def inherits_from(obj, a_class):
    """Checks and returns True if an object is an instance of a class
    Args:
    obj (any): the object that will be checked
    a_class (type): the class to match if the obj is of the same type"""
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    else:
        return False
