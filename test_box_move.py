from box_move import move_boxes, split_piles


# Prompt test cases
def test_move_boxes_scenario_1():
    assert (move_boxes(11, 2, 2)) == 7


def test_move_boxes_scenario_2():
    assert (move_boxes(3, 2, 5)) == 3


# My test cases
def test_split_piles():
    piles = split_piles(11, 2, 2)

    # Make sure no pile is over box carry limit
    for pile in piles:
        assert pile <= 2

    assert len(piles) == 7
