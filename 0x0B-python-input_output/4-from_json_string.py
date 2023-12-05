#!/usr/bin/python3
"""A a function that returns an object represented by a JSON string"""
from json import loads


def from_json_string(my_str):
    """checks and returns a python object represnted by a JSON string
    Args:
    my_str (str): json string to be checked"""
    return loads(my_str)
