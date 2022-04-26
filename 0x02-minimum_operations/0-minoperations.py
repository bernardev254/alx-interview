#!/usr/bin/python3
""" module containing a func to determine min ops"""


def minOperations(n: int) -> int:
    """func computing the min ops"""

    written = 1
    steps = 1
    clipboard = 1
    if n < 2:
        return 0

    steps += 1
    written += clipboard
    rem = n - written
    to_copy = written

    while rem > 0:
        if rem % to_copy == 0:
            if (rem - to_copy) % (to_copy + clipboard) == 0:
                # paste
                steps += 1
                written += clipboard
                rem = n - written
            else:
                # copy
                steps += 1
                clipboard = 0
                clipboard = to_copy = written
                # paste
                steps += 1
                written += clipboard
                rem = n - written
        else:
            # paste
            steps += 1
            written += clipboard
            rem = n - written

    return steps
