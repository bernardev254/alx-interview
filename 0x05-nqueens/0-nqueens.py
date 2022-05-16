#!/usr/bin/python3
"""module containing sol for n queen problem"""


import sys


n = 0
sols = []
sol = []
col = 0


def inputs():
    """ check arguments passed through the terminal"""
    global n
    n = 0
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    return n


def board(n):
    """return a repr of chess board n*"""
    my_board = []
    for i in range(n):
        my_board1 = []
        for j in range(n):
            my_board2 = []
            my_board2 += [i]
            my_board2 += [j]
            my_board1.append(my_board2)
        my_board.append(my_board1)
    return my_board


def queens(boardlist, col, n):
    """solve the problem by backtracking"""
    global sol
    global sols
    if col < n:
        for row in range(n):
            if safety(boardlist, row, col, n):
                sol.append(boardlist[row][col])
                if col == (n - 1):
                    sols.append(sol.copy())
                    sol.remove(boardlist[row][col])
                    return sols
                queens(boardlist, col + 1, n)
                sol.remove(boardlist[row][col])
    return sols


def safety(boardlist, row, col, n):
    """checks is the queen is safe"""
    # check for  collision on row
    for j in range(col):
        if boardlist[row][j] in sol:
            return False

    # check for collision on right diagonal
    i, j = row, col
    while i >= 0 and j >= 0:
        if boardlist[i][j] in sol:
            return False

        i -= 1
        j -= 1

    # check for collision on left diagonal
    x, y = row, col
    while x < n and y >= 0:
        if boardlist[x][y] in sol:
            return False

        x += 1
        y -= 1

    return True

inputs()
boardlist = board(n)
queens(boardlist, col, n)

for s in sols:
    print(s)
