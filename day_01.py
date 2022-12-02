#  --- Day 1: Calorie Counting ---
# %% Initialization


# %% Read input
with open("day_01_input.txt") as data:
    calories = [[int(x) for x in y.split("\n")] for y in
                data.read().strip().split("\n\n")]

# %% Part 1
print("Sum calories for top elf:", max(sum(x for x in y) for y in calories))

# %% Part 2
top3_sum = sum(sorted(sum(x for x in y) for y in calories)[-3:])
print("Sum of calories for top three elves:", top3_sum)

