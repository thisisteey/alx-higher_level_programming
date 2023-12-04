#!/usr/bin/python3
"""A function that returns the list of available attributes
and methods of an object"""


def lookup(obj):
    """Gets and returns the list of availabel attributes and methods
    of an object"""
    return (dir(obj))
