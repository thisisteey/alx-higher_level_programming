#!/usr/bin/python3
# function that multiplies 2 matrices by using the module NumPy
"""A function that multiplies two matrices using the NumPy module"""
import numpy as nump


def lazy_matrix_mul(m_a, m_b):
    """Returns the multiplication of two matrices in an array of lists
    Args:
    m_a (list of lists of integers or floats): first matrix
    m_b (list of lists of integers or floats): second matrix"""
    mbvalerr = "shapes (2,2) and (1,0) not aligned: 2 (dim 1) != 1 (dim 0)"
    mavalerr = "shapes (1,0) and (2,2) not aligned: 0 (dim 1) != 2 (dim 0)"
    lsterrma = "shapes (1,2) and (1,2) not aligned: 2 (dim 1) != 1 (dim 0)"
    lsterrmb = "shapes (2,2) and (2,2) not aligned: 2 (dim 1) != 2 (dim 0)"
    if type(m_a) != list:
        raise TypeError("Scalar operands are not allowed, use '*' instead")
    if type(m_b) != list:
        raise TypeError("Scalar operands are not allowed, use '*' instead")
    if not all(isinstance(rows, list) for rows in m_a):
        raise TypeError(lsterrma)
    if not all(isinstance(rows, list) for rows in m_b):
        raise TypeError(lsterrmb)
    if m_a == [] or m_a == [[]]:
        raise ValueError(mavalerr)
    if m_b == [] or m_b == [[]]:
        raise ValueError(mbvalerr)
    if not all(len(rows) == len(m_a[0]) for rows in m_a):
        raise ValueError("setting an array element with a sequence.")
    if not all(len(rows) == len(m_b[0]) for rows in m_b):
        raise ValueError("setting an array element with a sequence.")
    for rows in m_a:
        for col in rows:
            if type(col) != int and type(col) != float:
                raise TypeError("invalid data type for einsum")
    for rows in m_b:
        for col in rows:
            if type(col) != int and type(col) != float:
                raise TypeError("invalid data type for einsum")
    return nump.matmul(m_a, m_b)
