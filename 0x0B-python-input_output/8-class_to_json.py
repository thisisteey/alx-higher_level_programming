#!/usr/bin/python3
"""A python class-to-JSON function"""


def class_to_json(obj):
    """checks and return the dictionary representation of data struct"""
    return obj.__dict__
