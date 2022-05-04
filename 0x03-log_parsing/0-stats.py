#!/usr/bin/python3
"""script tha reads stdin and computes metrics"""


import sys
from collections import OrderedDict


def my_split(line):
    """my split func"""
    my_list = []
    for word in line.strip().split(" "):
        my_list.append(word)

    return my_list


def status_tally(status, code):
    """func returning status tally"""
    try:
        status[code] += 1
    except KeyError:
        pass


def print_status(status):
    """func printing status code  frequency"""
    status = OrderedDict(sorted(status.items()))
    for k, v in status.items():
        if v is not 0:
            print("{}: {}".format(k, v))

if __name__ == "__main__":
    status = {"200": 0, "301": 0, "400": 0,
              "401": 0, "403": 0, "404": 0,
              "405": 0, "500": 0}

    times = 0
    size = 0

    try:
        for lines in sys.stdin:
            size += int(my_split(lines)[8])
            status_tally(status, my_split(lines)[7])

            if times is not 0 and times % 9 == 0:
                print("File size: {:d}".format(size))
                print_status(status)

            times += 1

    except KeyboardInterrupt:
        pass

    finally:
        print("File size: {:d}".format(size))
        print_status(status)
        sys.exit(0)
