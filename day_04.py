#  --- Day 4: Camp Cleanup ---
# %% Initialization

# %% Read input
with open("day_04_input.txt") as data:
    assignments = [[*map(int, x.replace("-", ",").split(","))] for x in data]

# %% Part 1
print("Contained assignments:",
      sum(a <= c <= d <= b or c <= a <= b <= d for a, b, c, d in assignments))

# %% Part 2
print("Overlapping assignments:", sum(a <= d and b >= c for a, b, c, d in assignments))
