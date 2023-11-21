#!/usr/bin/python3
"""A class Square that defines a square by: (based on 6-square.py)"""


class Square:
    """A square class represented"""
    def __init__(self, size=0, position=(0, 0)):
        """initializes the square class
        Args:
        size (int): the size of the square
        position (int, int): the position of the square"""
        self.size = size
        self.position = position

    @property
    def size(self):
        """gets and returns the current size of the square"""
        return (self.__size)

    @size.setter
    def size(self, value):
        """sets the square size"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """gets and returns the current position of the square"""
        return (self.__position)

    @position.setter
    def position(self, value):
        """sets the square position"""
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(dig, int) for dig in value) or
                not all(dig >= 0 for dig in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """calculates and returns the current area of the square"""
        return (self.__size * self.__size)

    def my_print(self):
        """prints square in # char"""
        if self.__size == 0:
            print("")
            return
        [print("") for x in range(0, self.__position[1])]
        for x in range(0, self.__size):
            [print(" ", end="") for y in range(0, self.__position[0])]
            [print("#", end="") for z in range(0, self.__size)]
            print("")

    def __str__(self):
        """returns a string representation of the square"""
        if self.__size != 0:
            [print("") for x in range(0, self.__position[1])]
        for x in range(0, self.__size):
            [print(" ", end="") for y in range(0, self.__position[0])]
            [print("#", end="") for z in range(0, self.__size)]
            if x != self.__size - 1:
                print("")
        return ("")

