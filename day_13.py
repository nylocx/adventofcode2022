#  --- Day 13: Distress Signal ---
# %% Initialization
from itertools import zip_longest
from functools import cmp_to_key


def compare(a, b):
    # print("Comparing", a, "vs", b)
    if a is None:
        return True
    elif b is None:
        return False
    elif isinstance(a, int) and isinstance(b, int):
        return a < b if a != b else None
    elif isinstance(a, int) and isinstance(b, list):
        return compare([a], b)
    elif isinstance(a, list) and isinstance(b, int):
        return compare(a, [b])
    else:
        for x, y in zip_longest(a, b):
            if (r := compare(x, y)) is None:
                continue
            else:
                return r


# %% Read input
with open("day_13_input.txt") as data:
    pairs = [list(map(eval, x.split())) for x in data.read().strip().split("\n\n")]

# %% Part 1
print(
    "Sum of wrong ordered pairs:",
    sum(i + 1 for i, (a, b) in enumerate(pairs) if compare(a, b)),
)

# %% Part 2
packets = [x for y in pairs for x in y] + [[[2]], [[6]]]
sorted_packages = sorted(
    packets, key=cmp_to_key(lambda a, b: -1 if compare(a, b) else 1)
)
print(
    "Decoder Key:",
    (sorted_packages.index([[2]]) + 1) * (sorted_packages.index([[6]]) + 1),
)
