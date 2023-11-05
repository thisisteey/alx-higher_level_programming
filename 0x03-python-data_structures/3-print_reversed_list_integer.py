#!/usr/bin/python3
# function that prints all integers of a list in reverse order
# using def print_reversed_list_integer(my_list=[]) prototype

def print_reversed_list_integer(my_list=[]):
    if my_list:
        for num in reversed(my_list):
            print("{:d}".format(num))
