#!/usr/bin/python3
# function that prints a matrix of integers
# using def print_matrix_integer(matrix=[[]]) prototype

def print_matrix_integer(matrix=[[]]):
    for tup in matrix:
        for att in tup:
            print("{:d}".format(att), end=" " if att != tup[-1] else "")
        print()
