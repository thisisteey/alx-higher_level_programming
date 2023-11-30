#!/usr/bin/python3
# function that divides all elements of a matrix
"""A function that divides all elements of a matrix by a given number"""


def matrix_divided(matrix, div):
    """matrix_divided function intialized
    Args:
    matrix (list): matrix to be divied, represented as a list of lists
    div (int or float): divisor number to be used
    Errors to raise:
    TypeError: 1. for non-list matrix
                2. for unequal matrix rows size
                3. for non numeric divisor
    ZeroDivisionError: for when divisor is zero"""
    matsize = [0, 0]
    funcres = []
    list_err = "matrix must be a matrix (list of lists) of integers/floats"
    matrow_err = "Each row of the matrix must have the same size"
    if not isinstance(matrix, list):
        raise TypeError(list_err)
    matsize[0] = len(matrix)
    if matsize[0] == 0:
        raise TypeError(list_err)
    for rows in matrix:
        if not isinstance(rows, list):
            raise TypeError(list_err)
        elif len(rows) == 0:
            raise TypeError(list_err)
        else:
            if matsize[1] == 0:
                matsize[1] = len(rows)
            elif len(rows) != matsize[1]:
                raise TypeError(matrow_err)
            for columns in rows:
                if not isinstance(columns, (int, float)):
                    raise TypeError(list_err)
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    elif div == 0:
        raise ZeroDivisionError("division by zero")
    else:
        for rows in matrix:
            rowsresult = list(map(lambda t: round(t / div, 2), rows))
            funcres.append(rowsresult)
        return funcres
