#!/usr/bin/python3
# adds all unique integers in a list (only once for each integer)
# using def uniq_add(my_list=[]) prototype

def uniq_add(my_list=[]):
    uniquelst = set(my_list)
    fig = 0
    for num in uniquelst:
        fig += num
    return (fig)
