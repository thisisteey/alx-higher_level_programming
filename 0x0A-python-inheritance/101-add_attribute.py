#!/usr/bin/python3
"""A function that adds a new attribute to an object"""


def add_attribute(obj, att, value):
    """Adds a new attribute to an object if it’s possible
    Args:
    obj (any): object to an attribute to
    att (str): name of the attribute to add to the object
    value (any); the value of the attribute"""
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    else:
        setattr(obj, att, value)
