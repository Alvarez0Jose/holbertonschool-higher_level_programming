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
