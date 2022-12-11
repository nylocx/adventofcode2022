#  --- Day 9: Rope Bridge ---
# %% Initialization
import math

# %% Read input
with open("day_09_input.txt") as data:
    instructions = [tuple(x.split()) for x in data.read().strip().split("\n")]

# %% Part 1
h_pos = 0j
t_pos = 0j
tail_moves = {0j}

moves = {"U": 1j, "D": -1j, "R": 1, "L": -1}

for direction, steps in instructions:
    for step in range(int(steps)):
        h_pos += moves[direction]
        delta_pos = h_pos - t_pos
        if abs(delta_pos) > 1.5:
            dx = math.copysign(1, delta_pos.real) if delta_pos.real != 0 else 0
            dy = math.copysign(1, delta_pos.imag) if delta_pos.imag != 0 else 0
            delta_move = complex(dx, dy)
            t_pos += delta_move
            tail_moves.add(t_pos)
print("Unique positions of tail:", len(tail_moves))

# %% Part 2
positions = [0j for _ in range(10)]
tail_moves = {0j}

moves = {"U": 1j, "D": -1j, "R": 1, "L": -1}

for direction, steps in instructions:
    for step in range(int(steps)):
        positions[0] += moves[direction]
        for i, (h_pos, t_pos) in enumerate(zip(positions, positions[1:])):
            delta_pos = h_pos - t_pos
            if abs(delta_pos) > 1.5:
                dx = math.copysign(1, delta_pos.real) if delta_pos.real != 0 else 0
                dy = math.copysign(1, delta_pos.imag) if delta_pos.imag != 0 else 0
                delta_move = complex(dx, dy)
                positions[i + 1] += delta_move
                if i == 8:
                    tail_moves.add(positions[i + 1])
print("Unique positions of last tail knot:", len(tail_moves))
