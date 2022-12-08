#  --- Day 8: Treetop Tree House ---
# %% Initialization
from itertools import product

import numpy as np

# %% Read input
grid = np.genfromtxt("day_08_input.txt", np.uint8, delimiter=1)


# %% Part 1
height, width = grid.shape


def is_visible(x, y):
    if x == 0 or y == 0 or x == width - 1 or y == height - 1:
        return True
    tree_height = grid[y, x]
    left = grid[y, :x]
    right = grid[y, x + 1 :]
    top = grid[:y, x]
    bottom = grid[y + 1 :, x]
    return tree_height > min(np.max(left), np.max(right), np.max(top), np.max(bottom))


print(
    "Visible trees:",
    sum(is_visible(x, y) for x, y in product(range(height), range(width))),
)


# %% Part 2
def _score(tree_height, view):
    score = 0
    for v in view:
        score += 1
        if tree_height <= v:
            return score
    return score


def scenic_score(x, y):
    if x == 0 or y == 0 or x == width - 1 or y == height - 1:
        return 0
    tree_height = grid[y, x]
    left_score = _score(tree_height, reversed(grid[y, :x]))
    right_score = _score(tree_height, grid[y, x + 1 :])
    top_score = _score(tree_height, reversed(grid[:y, x]))
    bottom_score = _score(tree_height, grid[y + 1 :, x])
    return left_score * right_score * bottom_score * top_score


print(
    "Highest scenic score:",
    max(scenic_score(x, y) for x, y in product(range(height), range(width))),
)
