#!/usr/bin/python3
"""
Module creates a class named Base
"""

import json


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

    def save_to_file(cls, list_objs):
        """
        Method to save a file
        """
        filename = "{}.json".format(cls.__name__)
        list_dic = []

        if list_objs is not None:
            list_dic = [obj.to_dictionary() for obj in list_objs]

            Jstring = cls.to_json_string(list_dic)

            with open(filename, "w") as file:
                file.write(Jstring)
