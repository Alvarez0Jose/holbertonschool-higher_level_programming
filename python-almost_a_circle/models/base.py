#!/usr/bin/python3
"""
Module creates a class named Base
"""


class Base:
    """
    Class Base
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        Stating instances
        """
        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id

    def to_json_string(list_dictionaries):
        """
        Json String Method
        """
        if isinstance(list_dictionaries, list):
            if list_dictionaries is None or list_dictionaries == []:
                return "[]"
            else:
                Jstring = json.dumps(list_dictionaries)
        return Jstring
