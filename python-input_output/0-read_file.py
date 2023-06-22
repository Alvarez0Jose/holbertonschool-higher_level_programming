#!/usr/bin/python3

"""
This Module reads a Text and prints it to output
"""


def read_file(filename=""):
    """
    Function for reading and printing a file
    """
    with open(filename, "r") as file:
        content = file.read()
        print(content, end="")
