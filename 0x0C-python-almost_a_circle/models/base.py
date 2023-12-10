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
        if list_dictionaries is None or list_dictionaries == []:
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
            if list_objs is None:
                jfile.write("[]")
            else:
                lst_dicts = [obj.to_dictionary() for obj in list_objs]
                jfile.write(Base.to_json_string(lst_dicts))

    @staticmethod
    def from_json_string(json_string):
        """deserialize and returns a JSON string to a python list
        Args:
        json_string (str): JSON string representing a list of dictionaries"""
        if json_string is None or json_string == "[]":
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """instantiates and returns a class from a dictionary of attributes
        Args:
        **dictionary (dict): key/value pairs of attributes to be intialized"""
        if dictionary and dictionary != {}:
            if cls.__name__ == "Rectangle":
                newinst = cls(1, 1)
            else:
                newinst = cls(1)
            newinst.update(**dictionary)
            return (newinst)
