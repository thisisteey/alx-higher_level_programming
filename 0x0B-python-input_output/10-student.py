#!/usr/bin/python3
"""A class Student that defines a student by: (based on 9-student.py)"""


class Student:
    """Representing the student defined"""

    def __init__(self, first_name, last_name, age):
        """Intializing a student
        Args:
        first_name (str): first name of the student
        last_name (str): last name of the student
        age (int): age of the student"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """gets the dictionary represntation of the student
        Args:
        attrs (list): the attributes to represent (optional)"""
        if (type(attrs) == list and
                all(type(ele) == str for ele in attrs)):
            return {x: getattr(self, x) for x in attrs if hasattr(self, x)}
        else:
            return self.__dict__
