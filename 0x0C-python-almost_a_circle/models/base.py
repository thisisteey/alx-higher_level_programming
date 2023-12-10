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

    @classmethod
    def save_to_file(cls, list_objs):
        """serialize and write a list of objects to a file as JSON string
        Args:
        list_objs (list): the list of instances gotten from the base class"""
        fname = cls.__name__ + ".json"
        with open(fname, "w") as jfile:
            if not list_objs:
                jfile.write("[]")
            else:
                lst_dicts = [obj.to_dictionary() for obj in list_objs]
                jfile.write(Base.to_json_string(lst_dicts))
