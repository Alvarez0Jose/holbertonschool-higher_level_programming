#!/usr/bin/python3

"""
Module of 1 class and 2 public methods
"""


class BaseGeometry:
    """
    Class with a public Method
    """

    def area(self):
        """
        Method that raises an error message
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Public method that validates Values
        """
        if isinstance(name, str):
            if type(value) is not int:
                raise TypeError(f"{name} must be an integer")
            if value <= 0:
                raise ValueError(f"{name} must be greater than 0")


class Rectangle(BaseGeometry):
    """
    Class inherited from BaseGeomety
    """

    def __init__(self, width, height):
        """
        Method that sets new attributes private
        and validates they are positve integers
        """

        self.integer_validator("withd", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """
        Method used to return the area of the Rectangle
        """
        return self.__height * self.__width

    def __str__(self):
        """
        Method that returns a printable string
        """
        return f"[Rectangle] {self.__width}/{self.__height}"
