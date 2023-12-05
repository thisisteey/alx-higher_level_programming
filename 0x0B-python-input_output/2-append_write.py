#!/usr/bin/python3
"""A function that appends a string at the end of a text file (UTF8)"""


def append_write(filename="", text=""):
    """Appends a string to the end of a (UTF8) text file
    Args:
    filename (str): name of the file to append string to
    text (str): string to append to the file"""
    with open(filename, "a", encoding="utf-8") as fl:
        return fl.write(text)
