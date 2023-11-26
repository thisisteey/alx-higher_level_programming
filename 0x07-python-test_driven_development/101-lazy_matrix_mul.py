#!/usr/bin/python3
# function that multiplies 2 matrices by using the module NumPy
"""A function that multiplies two matrices using the NumPy module"""
import numpy as nump


def lazy_matrix_mul(m_a, m_b):
    """Returns the multiplication of two matrices in an array of lists
    Args:
    m_a (list of lists of integers or floats): first matrix
    m_b (list of lists of integers or floats): second matrix"""
    if type(m_a) != list:
        raise TypeError("m_a should be a list")
    if type(m_b) != list:
        raise TypeError("m_b should be a list")
    if not all(isinstance(rows, list) for rows in m_a):
        raise TypeError("m_a should be a list of lists")
    if not all(isinstance(rows, list) for rows in m_b):
        raise TypeError("m_b should be a list of lists")
    if m_a == [] or m_a == [[]]:
        raise ValueError("m_a should not be empty")
    if m_b == [] or m_b == [[]]:
        raise ValueError("m_b should not be empty")
    if not all(len(rows) == len(m_a[0]) for rows in m_a):
        raise ValueError("shapes (2,3) and (2,2) not aligned")
    if not all(len(rows) == len(m_b[0]) for rows in m_b):
        raise ValueError("shapes (2,2) and (2,3) not aligned")
    for rows in m_a:
        for col in rows:
            if type(col) != int and type(col) != float:
                raise TypeError("invalid data type in m_a for einsum")
    for rows in m_b:
        for col in rows:
            if type(col) != int and type(col) != float:
                raise TypeError("invalid data type in m_b for einsum")
    return nump.matmul(m_a, m_b)
