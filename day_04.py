#  --- Day 4: Camp Cleanup ---
# %% Initialization

# %% Read input
with open("day_04_input.txt") as data:
    assignments = [tuple(map(int, x.replace("-", ",").split(","))) for x in data]

# %% Part 1
print(sum((a >= c and b <= d) or (c >= a and d <= b) for a, b, c, d in assignments))

# %% Part 2
print(sum(d >= a >= c or d >= b >= c or b >= c >= a or b >= d >= a for a, b, c, d in
          assignments))
