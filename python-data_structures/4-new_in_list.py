#!/usr/bin/python3

def new_in_list(my_list, idx, element):

    if my_list is None:
        return

    New_List = my_list.copy()

    if idx < 0:
        return New_List

    elif idx >= len(New_List):
        return New_List

    else:
        New_List[idx] = element
        return New_List
