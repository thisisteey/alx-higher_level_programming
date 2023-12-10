#!/usr/bin/python3
"""A base class is defined"""
from json import dumps, loads
from csv import DictWriter, DictReader


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
            return dumps(list_dictionaries)

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
            return loads(json_string)

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

    @classmethod
    def load_from_file(cls):
        """loads class instance from a JSON file and returns a list instance"""
        fname = str(cls.__name__) + ".json"
        try:
            with open(fname, "r") as jfile:
                lst_dicts = Base.from_json_string(jfile.read())
                return [cls.create(**dct) for dct in lst_dicts]
        except IOError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """serialize and wrtie a list of objects to a file as CSV
        Args:
        list_objs (list): the list of instances gotten from the base class"""
        fname = cls.__name__ + ".csv"
        with open(fname, "w", newline="") as cfile:
            if list_objs is None or list_objs == []:
                cfile.write("[]")
            else:
                if cls.__name__ == "Rectangle":
                    fieldnames = ["id", "width", "height", "x", "y"]
                else:
                    fieldnames = ["id", "size", "x", "y"]
                cwriter = DictWriter(cfile, fieldnames=fieldnames)
                for objinst in list_objs:
                    cwriter.writerow(objinst.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        """loads class instance from a CSV file and returns a list instance"""
        fname = cls.__name__ + ".csv"
        try:
            with open(fname, "r", newline="") as cfile:
                if cls.__name__ == "Rectangle":
                    fieldnames = ["id", "width", "height", "x", "y"]
                else:
                    fieldnames = ["id", "size", "x", "y"]
                lst_dicts = DictReader(cfile, fieldnames=fieldnames)
                lst_dicts = [dict([key, int(val)] for key, val in dct.items())
                             for dct in lst_dicts]
                return [cls.create(**dct) for dct in lst_dicts]
        except IOError:
            return []
