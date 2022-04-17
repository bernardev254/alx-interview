#!/usr/bin/python3
"""module containing a function to determine if given boxes can all be
   unlocked with keys inside """


def canUnlockAll(boxes):
    box_no = []
    locked_boxes = []
    my_dict = {0: 'unlocked'}

    # box numbers
    for box in range(0, len(boxes)):
        box_no.append(box)

    # box 0 is unlocked get the others
    for box in range(1, len(boxes)):
        locked_boxes.append(box)

    keys = []
    for values in boxes[0]:
        keys.append(values)

    for idx in locked_boxes:
        if idx in keys:
            for values in boxes[idx]:
                keys.append(values)
            my_dict[idx] = 'unlocked'

    for no in box_no:
        if no not in my_dict.keys():
            if no in keys:
                for values in boxes[no]:
                    keys.append(values)
                my_dict[no] = 'unlocked'

    if len(boxes) == len(my_dict):
        return True

    return False
