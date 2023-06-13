#!/usr/bin/python3


"""
This script creates a class for square

"""


class Square:
    """
    This class represents the square
    """

    def __init__(self, size=0):
        """
        Here we're creating the first method with size
        """

        if not isinstance(size, int):
            raise TypeError("size must be integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
