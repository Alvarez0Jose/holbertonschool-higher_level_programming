#!/usr/bin/python3

"""
Module returns JSON representation of an object
"""

import json


def to_json_string(my_obj):
    """
    Function converts an object to a json string
    """
    JSON_string = json.dumps(my_obj)
    return JSON_string
