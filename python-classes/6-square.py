#!/usr/bin/python3

"""
Creating a Class Square
"""


class Square:
    """
    Square class
    """

    def __init__(self, size=0, position=(0, 0)):
        """
        creating the first method
        """
        self.__size = size
        self.__position = position

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
            for _ in range(self.__position[1]):
                print()
            for _ in range(self.__size):
                print(" " * self.__position[0] + "#" * self.__size)

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

    @property
    def position(self):
        """
        position property line of code
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        Postition setting values
        """
        if not isinstance(value, tuple) or len(value) != 2 or not all(isinstance(i, int) for i in value) or not all(i >= 0 for i in value):
            raise TypeError("Position must be a tuple of 2 positive integers")
        self.__postition = value
