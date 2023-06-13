#!/usr/bin/python3


"""
This script create square class
"""


class Square:
    """
    Square class
    """

    def __init__(self, size=0):
        """
         Here we're creating the first method with size
        """

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """
        Area of the square
        """
        return self.__size ** 2
