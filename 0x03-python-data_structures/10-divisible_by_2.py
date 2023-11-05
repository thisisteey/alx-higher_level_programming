#!/usr/bin/python3
# finds all multiples of 2 in a list
# using def divisible_by_2(my_list=[]) prototype

def divisible_by_2(my_list=[]):
    return [num % 2 == 0 for num in my_list]
