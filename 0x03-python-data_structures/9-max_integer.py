#!/usr/bin/python3
# finds the biggest integer of a list
# using def max_integer(my_list=[]) prototype

def max_integer(my_list=[]):
    if len(my_list) == 0:
        return 'None'
    else:
        bigint = my_list[0]
        for num in my_list:
            if num > bigint:
                bigint = num
        return bigint
