#!/usr/bin/python3
"""A function that writes a string to a text file (UTF8) and
returns the number of characters written"""


def write_file(filename="", text=""):
    """writes a string to a UTF8 text file
    Args:
    filename (str): name of the file to write
    text (str): text to write into the file"""
    with open(filename, "w", encoding="utf-8") as fl:
        return fl.write(text)
