#  --- Day 2: Rock Paper Scissors ---
# %% Initialization
value_map = {"X": 1, "Y": 2, "Z": 3}
outcome_map = {
    "A X": 3,
    "A Y": 6,
    "A Z": 0,
    "B X": 0,
    "B Y": 3,
    "B Z": 6,
    "C X": 6,
    "C Y": 0,
    "C Z": 3,
}

counter_map = {
    "A X": "A Z",
    "A Y": "A X",
    "A Z": "A Y",
    "B X": "B X",
    "B Y": "B Y",
    "B Z": "B Z",
    "C X": "C Y",
    "C Y": "C Z",
    "C Z": "C X",
}

# %% Read input
with open("day_02_input.txt") as data:
    guide = data.read().strip().split("\n")

# %% Part 1
print("Total score following guide:",
      sum(outcome_map[x] + value_map[x[-1]] for x in guide)
      )

# %% Part 2
print("Total score following new guide:",
      sum(outcome_map[counter_map[x]] + value_map[counter_map[x][-1]] for x in guide)
      )
