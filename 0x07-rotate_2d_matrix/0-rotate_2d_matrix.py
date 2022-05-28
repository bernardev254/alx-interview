#!/usr/bin/python3
"""module for a func to rotate a 2D matrix"""


def rotate_2d_matrix(matrix):
    """rotate a 2D matrix"""
    matrix1 = []
    for i in range(len(matrix)):
        for j in range((len(matrix) - 1), -1, -1):
            matrix1.append(matrix[j][i])
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            matrix[i][j] = matrix1.pop(0)
