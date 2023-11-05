#!/usr/bin/python3
# function that replaces an element of a list to a particular position
# using def replace_in_list(my_list, idx, element) prototype

def replace_in_list(my_list, idx, element):
    if idx < 0 or idx >= len(my_list):
        return my_list
    my_list[idx] = element
    return my_list
