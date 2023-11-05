#!/usr/bin/python3
# removes all character c and C from a string
# using def no_c(my_string) prototype

def no_c(my_string):
    nstr = my_string.translate({ord(ch): None for ch in 'cC'})
    return nstr
