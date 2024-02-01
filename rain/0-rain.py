#!/usr/bin/python3
"""calculation"""


def rain(walls):
    """calculate rain"""
    if not walls:
        return 0

    n = len(walls)
    left_side = [0] * n
    right_side = [0] * n

    left_side[0] = walls[0]
    for i in range(1, n):
        left_side[i] = side(left_side[i - 1], walls[i])

    right_side[n - 1] = walls[n - 1]
    for i in range(n - 2, -1, -1):
        right_side[i] = side(right_side[i + 1], walls[i])

    drops = 0
    for i in range(n):
        drops += min(left_side[i], right_side[i]) - walls[i]

    return drops if drops > 0 else 0