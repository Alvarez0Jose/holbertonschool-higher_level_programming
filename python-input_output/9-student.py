#!/usr/bin/python3

"""
Module retrieves a dictionary representation
of a student
"""


class Student:
    """
    Class defining Student
    """

    def __init__(self, first_name, last_name, age):
        """
        Method holds students values
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """
        Method returns a dictionary
        """
        return {'first_name': self.first_name,
                'last_name': self.last_name,
                'age': self.age
                }
