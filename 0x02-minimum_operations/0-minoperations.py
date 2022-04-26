#!/usr/bin/python3
""" module containing a func to determine min ops"""


def minOperations(n: int) -> int:
    """func computing the min ops"""

    rem = n
    steps = 0
    tasks = 2

    while (tasks < rem + 1):
        while rem % tasks == 0:
            steps += tasks
            rem /= tasks
        tasks += 1

    return steps
