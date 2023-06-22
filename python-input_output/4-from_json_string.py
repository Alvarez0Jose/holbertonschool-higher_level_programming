#!/usr/bin/python3

"""
Module converts a JSON string to an object
"""

import json


def from_json_string(my_str):
    """
    Function convers JSON string to an object
    """
    MyObject = json.loads(my_str)
    return MyObject
