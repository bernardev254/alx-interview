#!/usr/bin/python3
"""
module for island_perimeter() function
"""


def recur(a, b, matrix, my_dict):
    """recursion to find an island"""
    steps = [
        (0, 1),
        (1, 0),
        (0, -1),
        (-1, 0)
        ]
    for (ax, bx) in steps:
        new_a = ax + a
        new_b = bx + b
        if outside_grid(new_a, new_b, matrix):
            continue
        neibour = matrix[new_a][new_b]
        key = '{}{}'.format(a, b)
        if neibour == 1 and not (key in my_dict):
            recur(a, b, matrix, my_dict)


def outside_grid(a, b, matrix):
    """function to eliminate out of bounds error"""
    if a < 0 or b < 0 or a > len(matrix) - 1 or b > len(matrix) - 1:
        return True
    return False


def island_perimeter(grid):
    """
    Computes the length of the perimeter of an island.
    """
    in_island = {}
    for x, row in enumerate(grid):
        for y, cell in enumerate(row):
            if cell == 1:
                in_island['{}{}'.format(x, y)] = 'True'
                recur(x, y, grid, in_island)

    return len(in_island) * 2 + 2
