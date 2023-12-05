#!/usr/bin/python3
"""A script that adds all arguments to a Python list and save them to a file"""
from sys import argv

if __name__ == "__main__":
    save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
    load_from_json_file = \
        __import__('6-load_from_json_file').load_from_json_file

    try:
        elem = load_from_json_file("add_item.json")
    except FileNotFoundError:
        elem = []
    elem.extend(argv[1:])
    save_to_json_file(elem, "add_item.json")
