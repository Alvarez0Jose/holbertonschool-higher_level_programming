#!/usr/bin/python3
"""
This Functions returns True if the
object is exactly and instance
"""


def is_same_class(obj, a_class):
    """
    Comparing function
    """
    if type(obj) is a_class:
        if isinstance(obj, a_class):
            return True
        else:
            return False
