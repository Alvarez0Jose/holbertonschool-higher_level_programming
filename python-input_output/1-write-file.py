#!/usr/bin/python3

"""
Module to write a string to text, returns the
amount of charaters written
"""


def write_file(filename="", text=""):
    """
    Function that writes and counts characters
    """
    with open(filename, "Text") as file:
        return file.write(text)
