#!/usr/bin/python3
# function that retrieves an element from a list
# using def element_at(my_list, idx) prototype

def element_at(my_list, idx):
    if idx < 0 or idx >= len(my_list):
        return 'None'
    else:
        return my_list[idx]
