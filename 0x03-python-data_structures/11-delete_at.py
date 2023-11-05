#!/usr/bin/python3
# deletes thhe item at a position in a list
# using def delete_at(my_list=[], idx=0) prototype

def delete_at(my_list=[], idx=0):
    if idx < 0 or idx >= len(my_list):
        return my_list
    else:
        del my_list[idx]
    return my_list
