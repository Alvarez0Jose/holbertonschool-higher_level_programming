#!/usr/bin/python3

"""
Creating a Class Square
"""


class Square:
    """
    Square class
    """

    def __init__(self, size=0):
        """
        creating the first method
        """
            self.__size = size

    @property
    def size(self):

        """
        retrieves the size of the square
        """
        return self.__size

    @size.setter
    def size(self, value):

         """
         Sets size of the value
         """
         if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        Area of the square
        """
        return self.__size ** 2
