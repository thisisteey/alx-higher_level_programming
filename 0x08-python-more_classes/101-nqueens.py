#!/usr/bin/python3
"""A program that solves the N queens problem of placing non-attacking
queens on an NxN chessboard"""
from sys import argv, exit


def start_board(n):
    """initialize an n x n sized chessboard
    Args:
    brd (list): list of lists representing the chessboard"""
    brd = []
    [brd.append([]) for x in range(n)]
    [rows.append(' ') for x in range(n) for rows in brd]
    return (brd)


def cpy_board(brd):
    """returns a copy of the chessboard
    Args:
    brd (list): list of lists representing the chessboard"""
    if isinstance(brd, list):
        return list(map(cpy_board, brd))
    return (brd)


def get_queenspos(brd):
    """gets and returns a solved chessboard
    Args:
    brd (list): list of lists representing the chessboard"""
    sol = []
    for y in range(len(brd)):
        for z in range(len(brd)):
            if brd[y][z] == "Q":
                sol.append([y, z])
                break
    return (sol)


def mark_spot(brd, rows, cols):
    """marks spots where non-attacking queen cannot play
    Args:
    brd (list): the chessboard
    rows (int): last played queen row
    cols (int): last played queen column"""
    for z in range(cols + 1, len(brd)):
        brd[rows][z] = "x"
    for z in range(cols - 1, -1, -1):
        brd[rows][z] = "x"
    for y in range(rows + 1, len(brd)):
        brd[y][cols] = "x"
    for y in range(rows - 1, -1, -1):
        brd[y][cols] = "x"
    z = cols + 1
    for y in range(rows + 1, len(brd)):
        if z >= len(brd):
            break
        brd[y][z] = "x"
        z += 1
    z = cols - 1
    for y in range(rows - 1, -1, -1):
        if z < 0:
            break
        brd[y][z]
        z -= 1
    z = cols + 1
    for y in range(rows - 1, -1, -1):
        if z >= len(brd):
            break
        brd[y][z] = "x"
        z += 1
    z = cols - 1
    for y in range(rows + 1, len(brd)):
        if z < 0:
            break
        brd[y][z] = "x"
        z -= 1


def solve_nqueens(brd, rows, qun, sol):
    """solves an N-queens puzzle recursively
    Args:
    brd (list): the chessboard
    rows (int): the current working row
    qun (int): the number of placed queens
    sol (list): list of lists of solutions"""
    if qun == len(brd):
        sol.append(get_queenspos(brd))
        return (sol)
    for z in range(len(brd)):
        if brd[rows][z] == " ":
            tempbrd = cpy_board(brd)
            tempbrd[rows][z] = "Q"
            mark_spot(tempbrd, rows, z)
            sol = solve_nqueens(tempbrd, rows + 1, qun + 1, sol)
    return (sol)


if __name__ == "__main__":
    if len(argv) != 2:
        print("Usage: nqueens N")
        exit(1)
    if not argv[1].isdigit():
        print("N must be a number")
        exit(1)
    if int(argv[1]) < 4:
        print("N must be at least 4")
        exit(1)
    brd = start_board(int(argv[1]))
    sol = solve_nqueens(brd, 0, 0, [])
    for s in sol:
        print(s)
