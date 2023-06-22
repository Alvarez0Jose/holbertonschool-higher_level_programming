#!/usr/bin/python3

"""
Module that writes an object to a file
"""

import json


def save_to_json_file(my_obj, filename):
    """
    Function that writes an object to a file
    """
    with open(filename, "w") as file:
        json.dump(my_obj, file)
