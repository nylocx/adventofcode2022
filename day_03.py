#  --- Day 3: Rucksack Reorganization ---
# %% Initialization

# %% Read input
with open("day_03_input.txt") as data:
    rucksacks = [[ord(x) - (96 if x.islower() else 38) for x in s.strip()] for s in data]

# %% Part 1
print("Sum of shared items:",
      sum(set(x[:len(x) // 2]).intersection(set(x[len(x) // 2:])).pop() for x in
          rucksacks)
      )

# %% Part 2
print("Sum of badges:",
      sum(set.intersection(*[set(x) for x in rucksacks[i:i + 3]]).pop() for i in
          range(0, len(rucksacks), 3)))

# %% Part 2 short version
print("Sum of badges:",
      sum(set.intersection(*map(set, x)).pop() for x in zip(*[iter(rucksacks)] * 3)))
