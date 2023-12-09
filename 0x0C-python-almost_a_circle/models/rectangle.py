#!/usr/bin/python3
"""A rectangle class inherited from Base is defined"""
from models.base import Base


class Rectangle(Base):
    """Representing the defined rectangle"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initializing the rectangle class
        Args:
        width (int): the width of the rectangle
        height (int): the height of the rectangle
        x (int): sets the x-coordinate of the rectangle
        y (int): sets the y-coordinate of the rectangle
        id (int): assigns an identifier to the rectangle"""
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """gets and returns the width of the rectangle"""
        return (self.__width)

    @width.setter
    def width(self, dig):
        """sets the rectangle width"""
        if type(dig) is not int:
            raise TypeError("width must be an integer")
        if dig <= 0:
            raise ValueError("width must be > 0")
        self.__width = dig

    @property
    def height(self):
        """gets and returns the height of the rectangle"""
        return (self.__height)

    @height.setter
    def height(self, dig):
        """sets the rectangle height"""
        if type(dig) is not int:
            raise TypeError("height must be an integer")
        if dig <= 0:
            raise ValueError("height must be > 0")
        self.__height = dig

    @property
    def x(self):
        """gets and returns the x coordnate of the rectangle"""
        return (self.__x)

    @x.setter
    def x(self, dig):
        """sets the x coordinate of the rectangle"""
        if type(dig) is not int:
            raise TypeError("x must be an integer")
        if dig < 0:
            raise ValueError("x must be >= 0")
        self.__x = dig

    @property
    def y(self):
        """gets and returns the y coordinate of the rectangle"""
        return (self.__y)

    @y.setter
    def y(self, dig):
        """sets the y coordinate of the rectangle"""
        if type(dig) is not int:
            raise TypeError("y must be an integer")
        if dig < 0:
            raise ValueError("y must be >= 0")
        self.__y = dig

    def area(self):
        """calculates and returns the area of the rectangle"""
        return (self.__width * self.__height)
