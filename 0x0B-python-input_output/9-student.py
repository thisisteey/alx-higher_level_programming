#!/usr/bin/python3
"""A class Student that defines a student"""


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

    def to_json(self):
        """gets and returns the dictionary represntation of the student"""
        return self.__dict__
