#!/usr/bin/python3
"""
Module creates a Rectangle class that inherets form Base
"""

from models.base import Base


class Rectangle(Base):
    """
    Class Rectangle inheriting from Base
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Method for creating a rectangle
        Parameters:
            width
            height
        """
        if type(width) is not int:
            raise TypeError("width must be an integer")
        self.width = width

        if type(height) is not int:
            raise TypeError("height must be an integer")
        self.height = height

        if type(x) is not int:
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        self.x = x

        if type(y) is not int:
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        self.y = y

        super().__init__(id)
