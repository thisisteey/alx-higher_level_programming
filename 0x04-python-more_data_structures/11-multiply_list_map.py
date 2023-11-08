#!/usr/bin/python3
# returns a list with all values multiplied by a number without using any loops
# using def multiply_list_map(my_list=[], number=0) prototype

def multiply_list_map(my_list=[], number=0):
    return list(map((lambda elm: elm*number), my_list))
