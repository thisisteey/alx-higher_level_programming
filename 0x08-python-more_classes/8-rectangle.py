#!/usr/bin/python3
"""A class Rectangle that defines a rectangle by: (based on 6-rectangle.py)"""


class Rectangle:
    """A rectangle class represented"""
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """initialise the rectangle class
        Args:
        width (int): the width of the rectangle
        height (int): the height of the rectangle"""
        type(self).number_of_instances += 1
        self.width = width
        self.height = height

    @property
    def width(self):
        """gets and returns the width of the rectangle"""
        return (self.__width)

    @width.setter
    def width(self, value):
        """sets the rectangle width"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """gets and returns the height of the rectangle"""
        return (self.__height)

    @height.setter
    def height(self, value):
        """sets the rectangle height"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """calculates and returns the area of the rectangle"""
        return (self.__width * self.__height)

    def perimeter(self):
        """calcualtes and returns the perimeter of the rectangle"""
        if self.__width == 0 or self.__height == 0:
            return (0)
        return ((self.__width * 2) + (self.__height * 2))

    def __str__(self):
        """prints the rectangle using the # char"""
        if self.__width == 0 or self.__height == 0:
            return ("")
        rec = []
        for x in range(self.__height):
            [rec.append(str(self.print_symbol)) for y in range(self.__width)]
            if x != self.__height - 1:
                rec.append("\n")
        return ("".join(rec))

    def __repr__(self):
        """calculates and returns the string representation of the rectangle"""
        rec = "Rectangle(" + str(self.__width)
        rec += ", " + str(self.__height) + ")"
        return (rec)

    def __del__(self):
        """prints a message after deleting a rectangle"""
        print("Bye rectangle...")
        type(self).number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """calculates and returns the biggest rectangle based on area
        Args:
        rect_1 (Rectangle): the first rectangle
        rect_2 (Rectangle): the second rectangle"""
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return(rect_1)
        return (rect_2)
