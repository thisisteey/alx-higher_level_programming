#!/usr/bin/python3
"""A square class inherited from the rectangle class is defined"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Representing the the defined square"""

    def __init__(self, size, x=0, y=0, id=None):
        """Initializing the square class
        Args:
        size (int): the size of the square
        x (int): sets the x-coordinate of the square
        y (int): sets the y-coordinate of the square
        id (int): assigns an identifier to the square"""
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """gets and returns the size of the square"""
        return (self.width)

    @size.setter
    def size(self, dig):
        """sets the square size"""
        self.width = dig
        self.height = dig

    def __str__(self):
        """calculates and returns the string representation of the square"""
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y,
                                                 self.width)
