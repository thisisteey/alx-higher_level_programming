#!/usr/bin/python3
# returns a key with the biggest integer value
# using def best_score(a_dictionary) prototype

def best_score(a_dictionary):
    if not a_dictionary:
        return None
    return max(a_dictionary, key=a_dictionary.get)
