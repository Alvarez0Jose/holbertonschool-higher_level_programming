#!/usr/bin/python3

"""
Funtion that returns True if the object is an instance
of a specified class
"""


def inherits_from(obj, a_class):
    """
    Functions that returns True or False
    """
    return issubclass(type(obj), a_class) and type(obj) is not a_class
