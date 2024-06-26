"""
Below was added by prompt to input test scenario data.
Commented out since I'm using a unit test framework.

# import sys
# boxes = int(sys.stdin.readline())
# carry_limit = int(sys.stdin.readline())
# parts = int(sys.stdin.readline())
"""


def move_boxes(boxes: int, carry_limit: int, parts: int) -> int:
    """Calculate the number of piles to move boxes in a room

    Params:
        boxes (int) - total number of boxes in the room
        carry_limit (int) - number of boxes that can be carried at once
        parts (int) - number of parts to split (piles of zero size discarded)
    Returns (int) - number of piles you'll get in the end
    """

    # If total boxes are fewer than number of piles then the result is one pile
    # for each box after zero size piles are discarded
    if boxes < parts:
        return boxes

    total_piles = len(split_piles(boxes, carry_limit, parts))

    return total_piles


def split_piles(boxes: int, carry_limit: int, parts: int):
    # Start by splitting piles into equal parts via division
    piles = [int(boxes / parts)] * parts

    # Add one to a pile for each remainder
    for i in range(boxes % parts):
        piles[i] += 1

    final_piles = []

    for pile in piles:
        # If pile is above carry limit, split it again
        if pile > carry_limit:
            final_piles.extend(split_piles(pile, carry_limit, parts))

        else:
            final_piles.append(pile)

    return final_piles
