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
