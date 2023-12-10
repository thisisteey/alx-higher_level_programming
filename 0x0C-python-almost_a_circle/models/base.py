#!/usr/bin/python3
"""A base class is defined"""
import json


class Base:
    """Representing the defined base
    Private class attribute:
    __nb_objects (int): Count of created base instances"""

    __nb_objects = 0

    def __init__(self, id=None):
        """Initializing the base class
        Args:
        id (int): the identifier of the new base instance"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """serialize and returns a list of dicts to JSON string
        Args:
        list_dictionaries (list): the list of dictionaries to serialize"""
        if not list_dictionaries:
            return "[]"
        else:
            return json.dumps(list_dictionaries)
