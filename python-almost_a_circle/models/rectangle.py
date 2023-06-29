#!/usr/bin/python3
"""
Module creates a Rectangle class that inherets form Base
"""

from models.base import Base


class Rectangle(Base):
    """
    Class Rectangle inheriting from Base
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Method for creating a rectangle
        Parameters:
            width
            height
        """
        super().__init__(id)

        if type(width) is not int:
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        self.width = width

        if type(height) is not int:
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        self.height = height

        if type(x) is not int:
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        self.x = x

        if type(y) is not int:
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        self.y = y

        @property
        def width(self):
            """width property"""
            return self.__width

        @width.setter
        def width(self, value):
            """Width setter"""
            if not isinstance(value, int):
                raise TypeError("width must be an integer")
            if value <= 0:
                raise ValueError("width must be > 0")
            self.__width = value

        @property
        def height(self):
            """height property"""
            return self.__height

        @height.setter
        def height(self, value):
            """height setter"""
            if not isinstance(value, int):
                raise TypeError("height must be an integer")
            if value <= 0:
                raise ValueError("height must be > 0")
            self.__height = value

        @property
        def x(self):
            """x property"""
            return self.__x

        @x.setter
        def x(self, value):
            """x setter"""
            if not isinstance(value, int):
                raise TypeError("x must be an integer")
            if value < 0:
                raise ValueError(" x must be >= 0")
            self.__x = value

        @property
        def y(self):
            """y property"""
            return self.__y

        @y.setter
        def y(self, value):
            if not isinstance(value, int):
                raise TypeError("y must be an integer")
            if value < 0:
                raise ValueError("y must be >= 0")
            self.__y = value

        def area(self):
            """
            Returns the area of a Rectangle
            """
            return self.__width * self.__height

        def display(self):
            """
            Displays a Rectangle
            """
            rec = self.__y * "\n"
            for i in range(self.__height):
                rec += ("" * self.__x)
                rec += ("#" * self.__width) + "\n"
            print(rec, end="")

        def __str__(self):
            """
            Method for str
            """
            str_rec = "[Rectangle] "
            str_id = f"({self.id}) "
            str_xy = f"{self.__x}/{self.__y} - "
            str_hw = f"{self.__width}/{self.__height}"
            str_return = str_rec + str_id + str_xy + str_hw
            return str_return

        def update(self, *args, **kwargs):
            """
            Method to add arguments information
            to each attribute
            """
            if args:
                self.id = args[0]
                self.__width = args[1]
                self.__height = args[2]
                self.__x = args[3]
                self.__y = args[4]
            elif kwargs:
                for key, value in kwargs.items():
                    setattr(self, key, value)
