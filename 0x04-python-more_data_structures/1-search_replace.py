#!/usr/bin/python3
# replaces all occurrences of an element by another in a new list
# using def search_replace(my_list, search, replace) prototype

def search_replace(my_list, search, replace):
    nlist = list(map(lambda itm: replace if itm == search else itm, my_list))
    return (nlist)
