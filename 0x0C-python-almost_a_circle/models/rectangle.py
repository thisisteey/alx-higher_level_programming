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

    def display(self):
        """prints the rectangle using the # char"""
        if self.__width == 0 or self.__height == 0:
            print("")
            return
        [print("") for y in range(self.__y)]
        for h in range(self.__height):
            [print(" ", end="") for x in range(self.__x)]
            [print("#", end="") for w in range(self.__width)]
            print("")

    def __str__(self):
        """calculates and returns the string representation of the rectangle"""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id,
                                                       self.x, self.y,
                                                       self.width, self.height)

    def update(self, *args, **kwargs):
        """assigns an argument and key/value argument to the attributes
        Args:
        *args (int): attribute values to be added
            1st argument representing the id attribute
            2nd argument representing the width attribute
            3rd argument represnting the height attribute
            4th argument represnting the x attribute
            5th argumnet represnting the y attribute
        **kwargs (dict): key/value attributes to be added"""
        if args and len(args) != 0:
            ag = 0
            for arg in args:
                if ag == 0:
                    if arg is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = arg
                elif ag == 1:
                    self.width = arg
                elif ag == 2:
                    self.height = arg
                elif ag == 3:
                    self.x = arg
                elif ag == 4:
                    self.y = arg
                ag += 1
        elif kwargs and len(kwargs) != 0:
            for key, val in kwargs.items():
                if key == "id":
                    if val is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = val
                elif key == "width":
                    self.width = val
                elif key == "height":
                    self.height = val
                elif key == "x":
                    self.x = val
                elif key == "y":
                    self.y = val
