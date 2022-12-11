#  --- Day 10: Cathode-Ray Tube ---
# %% Initialization

# %% Read input
with open("day_10_input.txt") as data:
    program_code = data.read().strip().split("\n")

# %% Part 1
x = 1
program = program_code.copy()
cmd = program.pop(0)
processing = False
signals = []
for cycle in range(1, 221):
    if cycle in [20, 60, 100, 140, 180, 220]:
        print("Adding signal", cycle * x)
        signals.append(cycle * x)
    if cmd == "noop":
        print("Noop, continuing")
        cmd = program.pop(0)
        continue
    elif processing:
        print("Currently processing", cmd)
        x += processing
        processing = False
        cmd = program.pop(0)
    else:
        print("New command", cmd)
        processing = int(cmd.split()[1])


print(sum(signals))


# %% Part 2
program = program_code.copy()
x = 1
cmd = program.pop(0)
processing = False
cycle = 1
while program:
    px = cycle % 40
    cycle += 1
    if 0 <= px - x < 3:
        print("#", end="")
        # print(f"#{x:0>2}-{px:0>2}", end="")
    else:
        print(".", end="")
        # print(f".{x:0>2}-{px:0>2}", end="")
    if px == 0:
        print()
    if cmd == "noop":
        cmd = program.pop(0)
        continue
    elif processing:
        x += processing
        processing = False
        cmd = program.pop(0)
    else:
        processing = int(cmd.split()[1])
