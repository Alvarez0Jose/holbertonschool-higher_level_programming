#!/usr/bin/python3
"""Module: 1-Rectangle"""
"""
Creating a Rectangle class
"""

class Rectangle:
    """Rectangle class we're gonna be working on.
    """
    def __init__(self, width=0, height=0):
        """
        provides de parameters for width and height
        """
        self.width = width
        self.height = height

    @property
    """Creating a private Width"""
    def width(self):
        return self.__width

    @width.setter
    """Setting the Width parameters"""
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    """making a private height"""
    def height(self):
        return self.__height

    @height.setter
    """Setting the Height parameters"""
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >- 0")
        self.__height = value
