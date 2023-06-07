#!/usr/bin/python3

def new_in_line(my_list, idx, element):
    if my_list is None:
        return

    NewList = my_list.copy()

    if idx < 0:
        return NewList
    elif idx >= len(NewList):
        return NewList
    else:
        NewList[idx] = element
        return NewList
