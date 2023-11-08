#!/usr/bin/python3
# returns the weighted average of all integers tuple
# using def weight_average(my_list=[]) prototype

def weight_average(my_list=[]):
    if not my_list:
        return 0
    fig = 0
    dig = 0
    for num in my_list:
        fig += num[0] * num[1]
        dig += num[1]
    return (fig / dig)
