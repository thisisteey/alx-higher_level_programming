#!/usr/bin/python3
"""A function that writes an Object to a text file, as a JSON representation"""
from json import dump


def save_to_json_file(my_obj, filename):
    """Use JSON represntation to write an object to a text file"""
    with open(filename, "w") as fl:
        dump(my_obj, fl)
