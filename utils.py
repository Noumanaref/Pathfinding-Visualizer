import math


def manhattan(current, goal):
    row1, col1 = current
    row2, col2 = goal
    return abs(row1 - row2) + abs(col1 - col2)


def euclidean(current, goal):
    row1, col1 = current
    row2, col2 = goal
    return math.sqrt((row1 - row2) ** 2 + (col1 - col2) ** 2)