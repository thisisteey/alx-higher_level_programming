#!/usr/bin/python3
"""A base class is defined"""
from json import dumps, loads
from csv import DictWriter, DictReader
import turtle


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

    @staticmethod
    def draw(list_rectangles, list_squares):
        """using the imported turtle module to draw rectangles and squares
        Args:
        list_rectangles (list): list of rectangles to draw
        list_squares (list): list of squares to draw"""
        tutcol = turtle.Turtle()
        tutcol.screen.bgcolor("#808080")
        tutcol.pensize(2)
        tutcol.register_shape("heart", ((-30, -40), (0, 40), (30, -40)))
        tutcol.shape("heart")

        tutcol.color("#8F9779")
        for rec in list_rectangles:
            tutcol.showturtle()
            tutcol.up()
            tutcol.goto(rec.x, rec.y)
            tutcol.down()
            for side in range(2):
                tutcol.forwars(rec.width)
                tutcol.left(90)
                tut.forward(rec.height)
                tut.left(90)
            tutcol.hideturtle()

        tutcol.color("4682B4")
        for sqr in list_squares:
            tutcol.showturtle()
            tutcol.up()
            tutcol.goto(sqr.x, sqr.y)
            tutcol.down()
            for side in range(4):
                tutcol.forward(sqr.width)
                tutcol.left(90)
            tutcol.hideturtle()
        turtle.exitonclick()
