#!/usr/bin/python3

"""
Module has a function that appends to the end of
a text file
"""


def append_write(filename="", text=""):
    """
    Function that appends text
    """
    with open(filename, "a") as file:
        return file.write(text)
