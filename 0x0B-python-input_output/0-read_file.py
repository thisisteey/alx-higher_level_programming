#!/usr/bin/python3
"""A function that reads a text file (UTF8) and prints it to stdout"""


def read_file(filename=""):
    """Reads and prints the content of a text file to the stdout"""
    with open(filename, encoding="utf-8") as fl:
        print(fl.read(), end="")
