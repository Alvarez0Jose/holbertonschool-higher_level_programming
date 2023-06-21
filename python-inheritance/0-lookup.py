#!/usr/bin/python3
    """
    This function returns a list of attributes and methods available for an object
    """

def lookup(obj):
    """
    Lookup Function
    """
    i = list(dir(obj))
    return i
