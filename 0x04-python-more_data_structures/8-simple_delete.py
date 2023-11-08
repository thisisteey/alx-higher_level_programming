#!/usr/bin/python3
# deletes a key in a dictionary
# using def simple_delete(a_dictionary, key="") prototype

def simple_delete(a_dictionary, key=""):
    if key in a_dictionary:
        del a_dictionary[key]
    return a_dictionary
