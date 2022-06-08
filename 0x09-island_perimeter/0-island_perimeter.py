#!/usr/bin/python3
"""
module for island_perimeter() function
"""


def find_neibour(a, b, matrix, cell_perimeter):
    """finds the neibouring land in an island
       and calculate the perimeter based on who neibours
       a land -is it more land or water?- """
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
        if neibour == 1:
            cell_perimeter -= 1
    return cell_perimeter


def outside_grid(a, b, matrix):
    """function to eliminate out of bounds error"""
    if a < 0 or b < 0 or a > len(matrix) - 1 or b > len(matrix[0]) - 1:
        return True
    return False


def island_perimeter(grid):
    """
    Computes the length of the perimeter of an island.
    """
    perimeter = 0
    for x, row in enumerate(grid):
        for y, cell in enumerate(row):
            cell_perim = 0
            if cell == 1:
                cell_perim = 4
                cell_perim = find_neibour(x, y, grid, cell_perim)
            perimeter += cell_perim

    return perimeter
