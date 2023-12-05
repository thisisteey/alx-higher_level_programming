#!/usr/bin/python3
"""A function that defines the Pascal's Triangle"""


def pascal_triangle(n):
    """representing the defined pascal triangle
    Args:
    n: size of the triangle"""
    if n <= 0:
        return []
    pastri = [[1]]
    while len(pastri) != n:
        pt = pastri[-1]
        temp = [1]
        for x in range(len(pt) - 1):
            temp.append(pt[x] + pt[x + 1])
        temp.append(1)
        pastri.append(temp)
    return pastri
