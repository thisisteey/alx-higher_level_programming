#!/usr/bin/python3
# function that replaces an element in a list at a position without modifying the original
# using def new_in_list(my_list, idx, element) prototype

def new_in_list(my_list, idx, element):
    if idx < 0 or idx >= len(my_list):
        return my_list.copy()
    nlist = my_list.copy()
    nlist[idx] = element
    return nlist
