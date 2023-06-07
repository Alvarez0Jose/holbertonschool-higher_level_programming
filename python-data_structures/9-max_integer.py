#!/usr/bin/python3

def max_integer(my_list=[]):

    if my_list is None:
        return None

    if len(my_list) == 0:
        return None

    MaxInteger = sorted(my_list, reverse=True)

    return MaxInteger[0]
