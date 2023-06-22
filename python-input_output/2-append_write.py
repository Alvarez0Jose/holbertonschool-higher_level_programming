#!/usr/bin/python3

"""
Module has a function that appends to the end of
a text file
"""


def append_write(filename="", text=""):
    """
    Function that appends text
    """
    with open(filename, "Text") as file:
        return file.write(text)
