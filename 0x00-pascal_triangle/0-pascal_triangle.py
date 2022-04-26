#!/usr/bin/python3
""" module containing a fun to print pascal triangle"""


def pascal_triangle(n):
    """func to print pascal triangle"""
    list = []

    if n <= 0:
        return list
    list.append([1])
    for i in range(1, n):
        list.append([])
        list[i].append(1)
        for j in range(1, i):
            list[i].append(list[i - 1][j - 1] + list[i - 1][j])
        if (n != 0):
            list[i].append(1)

    return list
