#  --- Day :  ---
# %% Initialization
def message_position(msg: str, window_size: int) -> int:
    for i in range(len(msg) - window_size + 1):
        if len(set(msg[i : i + window_size])) == window_size:
            return i + window_size


# %% Read input
with open("day_06_input.txt") as data:
    message = data.read().strip()

# %% Part 1
print(message_position(message, 4))

# %% Part 2
print(message_position(message, 14))
