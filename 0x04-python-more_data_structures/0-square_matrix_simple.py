#!/usr/bin/python3
# computes the square value of all integers in a matrix
# using def square_matrix_simple(matrix=[]) prototype

def square_matrix_simple(matrix=[]):
    return [list(map((lambda elm: elm**2), row)) for row in matrix]
