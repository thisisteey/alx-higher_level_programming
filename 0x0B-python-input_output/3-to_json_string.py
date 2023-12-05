#!/usr/bin/python3
"""A function that returns the JSON representation of an object (string)"""
from json import dumps


def to_json_string(my_obj):
    """checks a string object and returns the JSON representation
    Args:
    my_obj (str): string object to check"""
    return dumps(my_obj)
