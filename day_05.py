#  --- Day 5: Supply Stacks ---
# %% Initialization
import re

# %% Read input
with open("day_05_input.txt") as data:
    init_stacks = None
    while line := data.readline().strip("\n"):
        crates = line[1::4]
        if init_stacks is None:
            init_stacks = [[] for _ in crates]
        for i, s in enumerate(crates):
            if s.isalpha():
                init_stacks[i].append(s)
    pattern = r"move (?P<move>\d+) from (?P<from>\d+) to (?P<to>\d+)"
    rules = [[int(i) for i in re.match(pattern, x).groups()] for x in data]

# %% Part 1
stacks = init_stacks.copy()
for move, _from, to in rules:
    to -= 1
    _from -= 1
    stacks[to] = stacks[_from][move - 1 :: -1] + stacks[to]
    stacks[_from] = stacks[_from][move:]
print("First crates (CrateMover 9000):", "".join(map(str, [x[0] for x in stacks])))

# %% Part 2
stacks = init_stacks.copy()
for move, _from, to in rules:
    to -= 1
    _from -= 1
    stacks[to] = stacks[_from][:move] + stacks[to]
    stacks[_from] = stacks[_from][move:]
print("First crates (CrateMover 9001):", "".join(map(str, [x[0] for x in stacks])))
