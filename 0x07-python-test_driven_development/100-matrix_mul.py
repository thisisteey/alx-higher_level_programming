#!/usr/bin/python3
# function that multiplies 2 matrices
"""A function that multiplies two matrices"""


def matrix_mul(m_a, m_b):
    """Args:
    m_a (list of lists of ints/floats): the first matrix
    m_b (list of lists of ints/floats): the second matrix
    Errors to raise:
    TypeError: 1. if either m_a or m_b is not a list
        2. if either m_a or m_b is not a list of lists
        3. if either m_a or m_b is not an integer or float
        4. if either m_a or m_b has different sized rows
    VakueError: 1. if either m_a or m_b is empty
        2. if either m_a or m_b cannot be multiplied"""
    if type(m_a) != list:
        raise TypeError("m_a must be a list")
    if type(m_b) != list:
        raise TypeError("m_b must be a list")
    if not all(isinstance(rows, list) for rows in m_a):
        raise TypeError("m_a must be a list of lists")
    if not all(isinstance(rows, list) for rows in m_b):
        raise TypeError("m_b must be a list of lists")
    if not all((isinstance(val, int) or isinstance(val, float))
            for val in [dig for rows in m_a for dig in rows]):
        raise TypeError("m_a should contain only integers or floats")
    if not all((isinstance(val, int) or isinstance(val, float))
            for val in [dig for rows in m_b for dig in rows]):
        raise TypeError("m_b should contain only integers or floats")
    if not all(len(rows) == len(m_a[0]) for rows in m_a):
        raise TypeError("each row of m_a must be of the same size")
    if not all(len(rows) == len(m_b[0]) for rows in m_b):
        raise TypeError("each row of m_b must be of the same size")

    if m_a == [] or m_a == [[]]:
        raise ValueError("m_a can't be empty")
    if m_b == [] or m_b == [[]]:
        raise ValueError("m_b can't be empty")
    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    transposed = []
    for mrow in range(len(m_b[0])):
        nerow = []
        for curridx in range(len(m_b)):
            nerow.append(m_b[curridx][mrow])
        transposed.append(nerow)

    nmat = []
    for rows in m_a:
        nerow = []
        for column in transposed:
            product = 0
            for x in range(len(transposed[0])):
                product += rows[x] * column[x]
            nerow.append(product)
        nmat.append(nerow)
    return nmat
