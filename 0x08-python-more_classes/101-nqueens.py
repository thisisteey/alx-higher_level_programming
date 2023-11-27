#!/usr/bin/python3
"""A program that solves the N queens problem"""


from sys import argv

if __name__ == "__main__":
    queenspos = []
    if len(argv) != 2:
        print("Usage: nqueens N")
        exit(1)
    if not argv[1].isdigit():
        print("N must be a number")
        exit(1)
    boardsz = int(argv[1])
    if boardsz < 4:
        print("N must be at least 4")
        exit(1)

    for rows in range(boardsz):
        queenspos.append([rows, None])

    def queen_exists(col):
        """checks that a queen is not in a column value"""
        for rows in range(boardsz):
            if col == queenspos[rows][1]:
                return True
        return False

    def reject_solution(currrow, currcol):
        """determines if solution will be rejected"""
        if (queen_exists(currcol)):
            return False
        idx = 0
        while(idx < currrow):
            if abs(queenspos[idx][1] - currcol) == abs(idx - currrow):
                return False
            idx += 1
        return True

    def clear_queenpos(strtrow):
        """clears the queen position from the point of failure"""
        for rows in range(strtrow, boardsz):
            queenspos[rows][1] = None

    def nqueens(currrow):
        """function to recursively bracktrack and find the solution"""
        for currcol in range(boardsz):
            clear_queenpos(currrow)
            if reject_solution(currrow, currcol):
                queenspos[currrow][1] = currcol
                if (currrow == boardsz - 1):
                    print(queenspos)
                else:
                    nqueens(currrow + 1)

    nqueens(0)
