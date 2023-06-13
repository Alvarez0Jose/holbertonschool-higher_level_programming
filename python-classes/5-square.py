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

    def area(self):
        """
        Area of the square
        """
        return self.__size ** 2

    def my_print(self):
        """
        Printing the Square
        """
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__size):
                print("#" * self.__size)

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
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
