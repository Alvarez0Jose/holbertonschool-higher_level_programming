#!/usr/bin/python3

"""
Module to create an object from a Json file
"""

import json


def load_from_json_file(filename):
    """
    Fucntion that creates an object
    """
    with open(filename, "r") as file:
        return json.load(file)
