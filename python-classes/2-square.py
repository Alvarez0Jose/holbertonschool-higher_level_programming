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

        Raises:
        TypeError: if size is not integer.
        ValueError: if size < 0
        """

        if not isinstance(size, int):
            raise TypeError("size must be integer")
        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size
