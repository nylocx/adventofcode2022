#  --- Day 14: Regolith Reservoir ---
# %% Initialization
import numpy as np

# %% Read input
with open("day_14_input.txt") as data:
    points = [
        np.array([list(map(int, y.split(","))) for y in x.split(" -> ")])
        for x in data.read().strip().split("\n")
    ]
width, height = np.max(np.concatenate(points), axis=0) + 1

# %% Part 1
wall = np.zeros((height, width), dtype=int)
for polyline in points:
    for (x1, y1), (x2, y2) in zip(polyline, polyline[1:]):
        wall[min(y1, y2) : max(y1, y2) + 1, min(x1, x2) : max(x1, x2) + 1] = 1

sand_count = 0
full = False
while not full:
    sand_count += 1
    at_rest = False
    x, y = 500, 0
    while not at_rest:
        if x + 1 >= width or x < 1 or y + 1 >= height:
            full = True
            break
        elif wall[y + 1, x] == 0:
            y += 1
        elif wall[y + 1, x - 1] == 0:
            y += 1
            x -= 1
        elif wall[y + 1, x + 1] == 0:
            y += 1
            x += 1
        else:
            wall[y, x] = 1
            at_rest = True

print(sand_count - 1)

# %% Part 2
height += 2
width = 500 + 2 * height
wall = np.zeros((height, width), dtype=int)
for polyline in points:
    for (x1, y1), (x2, y2) in zip(polyline, polyline[1:]):
        wall[min(y1, y2) : max(y1, y2) + 1, min(x1, x2) : max(x1, x2) + 1] = 1
wall[height - 1, :] = 1

sand_count = 0
full = False
while not full:
    sand_count += 1
    at_rest = False
    x, y = 500, 0
    while not at_rest:
        if wall[y, x] == 1:
            full = True
            break
        elif wall[y + 1, x] == 0:
            y += 1
        elif wall[y + 1, x - 1] == 0:
            y += 1
            x -= 1
        elif wall[y + 1, x + 1] == 0:
            y += 1
            x += 1
        else:
            wall[y, x] = 1
            at_rest = True

print(sand_count - 1)
