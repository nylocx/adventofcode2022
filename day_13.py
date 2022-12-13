#  --- Day 13: Distress Signal ---
# %% Initialization
from itertools import zip_longest
from functools import cmp_to_key


def compare(a, b):
    if a is None:
        return -1
    elif b is None:
        return 1
    elif isinstance(a, int) and isinstance(b, int):
        return -1 if a < b else 1 if b < a else 0
    elif isinstance(a, int) and isinstance(b, list):
        return compare([a], b)
    elif isinstance(a, list) and isinstance(b, int):
        return compare(a, [b])
    else:
        for x, y in zip_longest(a, b):
            if (r := compare(x, y)) == 0:
                continue
            return r
        return 0


# %% Read input
with open("day_13_input.txt") as data:
    pairs = [list(map(eval, x.split())) for x in data.read().strip().split("\n\n")]

# %% Part 1
print(
    "Sum of wrong ordered pairs:",
    sum(i + 1 for i, (a, b) in enumerate(pairs) if compare(a, b) < 0),
)

# %% Part 2
packets = [x for y in pairs for x in y] + [[[2]], [[6]]]
sorted_packages = sorted(packets, key=cmp_to_key(compare))
print(
    "Decoder Key:",
    (sorted_packages.index([[2]]) + 1) * (sorted_packages.index([[6]]) + 1),
)
