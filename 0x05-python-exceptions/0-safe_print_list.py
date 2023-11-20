#!/usr/bin/python3
# function that prints a specified number of elements from a list
# using def safe_print_list(my_list=[], x=0) prototype

def safe_print_list(my_list=[], x=0):
    elem = 0
    for idx in range(x):
        try:
            print(my_list[idx], end="")
            elem += 1
        except IndexError:
            break
    print("")
    return (elem)
