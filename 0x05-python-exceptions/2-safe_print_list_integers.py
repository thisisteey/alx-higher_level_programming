#!/usr/bin/python3
# function that prints first specified number of elements from a list
# using def safe_print_list_integers(my_list=[], x=0) prototype

def safe_print_list_integers(my_list=[], x=0):
    intprnt = 0
    for idx in range(x):
        try:
            print("{:d}".format(my_list[idx]), end="")
            intprnt += 1
        except ValueError:
            continue
        except TypeError:
            continue
    print("")
    return (intprnt)
