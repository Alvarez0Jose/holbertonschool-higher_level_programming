#!/usr/bin/python3

"""
Function to print Name
"""


def say_my_name(first_name, last_name=""):
    """
    Prints "My name is first name last name".

    Parameters:
    first_name: The first name
    last_name: The last name

    Raises:
    TypeError: If first_name is not a string or last_name is not a string.
    """

    # Validate first_name and last_name

    if not isinstance(first_name, str) or not isinstance(last_name, str):
        raise TypeError(
            "first_name must be a string or last_name must be a string")

    if last_name:
        print("My name is {} {}".format(first_name, last_name))
    else:
        print("My name is {}".format(first_name))
