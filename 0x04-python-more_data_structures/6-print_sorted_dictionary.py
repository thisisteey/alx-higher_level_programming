#!/usr/bin/python3
# prints a dictionary by ordered keys
# using def print_sorted_dictionary(a_dictionary) prototype

def print_sorted_dictionary(a_dictionary):
    sort_keys = sorted(a_dictionary.keys())
    for kys in sort_keys:
        print("{:s}: {}".format(kys, a_dictionary[kys]))
