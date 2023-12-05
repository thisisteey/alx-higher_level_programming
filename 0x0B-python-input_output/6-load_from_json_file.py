#!/usr/bin/python3
"""A function that creates an Object from a JSON file"""
from json import load


def load_from_json_file(filename):
    """use a JSON file tocreate a python object"""
    with open(filename) as fl:
        return load(fl)
