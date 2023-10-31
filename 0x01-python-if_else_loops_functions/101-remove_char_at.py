#!/usr/bin/python3
# creates a copy of a string and removes a character at a certain position
# using def remove_char_at(str, n) prototype

def remove_char_at(str, n):
    if n >= 0:
        nstr = str[:n] + str[n + 1:]
        return (nstr)
    else:
        return (str)
