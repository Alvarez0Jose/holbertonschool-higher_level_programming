#!/usr/bin/python3

def best_score(a_dictionary):
    if a_dictionary is None or not a_dictionary:
        return None

    MaxScore = float('-inf')
    BestKey = None

    for key, value in a_dictionary.items():
        if value > MaxScore:
            MaxScore = value
            BestKey = key

    return BestKey
