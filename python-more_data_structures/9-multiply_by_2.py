#!/usr/bin/python3

def multiply_by_2(a_dictionary):

    NewDictionary = {}

    for keys, value in a_dictionary.items():
        NewDictionary[keys] = value * 2

    return NewDictionary
