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

    def update(self, *args, **kwargs):
        """assigns an argument and key/value argument to the attributes
        Args:
        *args (int): attribute values to be added
            1st argument representing the id attribute
            2nd argument representing the size attribute
            3rd argument represnting the x attribute
            4th argument represnting the y attribute
        **kwargs (dict): key/value attributes to be added"""
        if args and len(args) != 0:
            ag = 0
            for arg in args:
                if ag == 0:
                    if arg is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = arg
                elif ag == 1:
                    self.size = arg
                elif ag == 2:
                    self.x = arg
                elif ag == 3:
                    self.y = arg
                ag += 1
        elif kwargs and len(kwargs) != 0:
            for key, val in kwargs.items():
                if key == "id":
                    if val is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = val
                elif key == "size":
                    self.size = val
                elif key == "x":
                    self.x = val
                elif key == "y":
                    self.y = val
