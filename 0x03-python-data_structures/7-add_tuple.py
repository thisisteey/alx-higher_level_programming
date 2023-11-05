#!/usr/bin/python3
#function that adds two tuples
# using def add_tuple(tuple_a=(), tuple_b()) prototype

def add_tuple(tuple_a=(), tuple_b=()):
    ntuple = ()
    tuple_1 = tuple_a + (0, 0)
    tuple_2 = tuple_b + (0, 0)
    ntuple = tuple_1[0] + tuple_2[0], tuple_1[1] + tuple_2[1]
    return ntuple
