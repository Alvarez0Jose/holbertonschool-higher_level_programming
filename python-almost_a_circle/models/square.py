#!/usr/bin/python3
"""
Module for a Square class to inheret from Rectangle
"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """
    Square class
    """

    def __init__(self, size, x=0, y=0, id=None):
        """
        Initializes intances
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """
        Method for Strs
        """
        str_square = "[Square] "
        str_id = f"({self.id}) "
        str_xy = f"{self.x}/{self.y} - "
        str_hw = f"{self.width}"
        str_return = str_square + str_id + str_xy + str_hw
        return str_return

    @property
    def size(self):
        """
        size getter
        """
        return self.width

    @size.setter
    def size(self, value):
        """
        Size setter
        """
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """
        Update Method
        """
        if args:
            self.id = args[0]
            self.size = args[1]
            self.x = args[2]
            self.y = args[3]
        elif kwargs:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """
        Method for dictionary
        """
        dictionary = {
            "id": self.id,
            "size": self.width,
            "x": self.x,
            "y": self.y
        }
        return dictionary
