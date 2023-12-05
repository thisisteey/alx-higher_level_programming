#!/usr/bin/python3
"""A function that inserts a line of text to a file"""


def append_after(filename="", search_string="", new_string=""):
    """inserts a text aftereach line containing a specific string
    Args:
    filename (str): name of the file
    search_string (str): string to search for in the file
    new_string (str): string to insert"""
    txt = ""
    with open(filename) as fl:
        for line in fl:
            txt += line
            if search_string in line:
                txt += new_string
    with open(filename, "w") as wl:
        wl.write(txt)
