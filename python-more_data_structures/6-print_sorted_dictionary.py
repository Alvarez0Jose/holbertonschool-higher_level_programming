#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):

    OrderOfKeys = sorted(a_dictionary.keys())

    for a in OrderOfKeys:
        print("{}: {}".format(a, a_dictionary[a]))
