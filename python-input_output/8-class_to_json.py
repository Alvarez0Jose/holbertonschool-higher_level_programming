#!/usr/bin/python3

"""
Module returns a dictionary description
"""


def class_to_json(obj):
    """
    Function that returns a dictionary
    """

    result = {}
    if hasattr(obj, "__dict__"):
        result = obj.__dict__.copy()
    return result
