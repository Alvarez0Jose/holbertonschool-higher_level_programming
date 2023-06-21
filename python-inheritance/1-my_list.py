#!/usr/bin/python3
"""
Class Mylist
"""


class MyList(list):
    """
    Class for sorting a list
    """

    def print_sorted(self):
        """
        Method tha sorts a list
        """
        if isinstance(self, list):
            SortedList = sorted(self)
            print(SortedList)
