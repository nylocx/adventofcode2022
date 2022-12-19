#  --- Day 15: Beacon Exclusion Zone ---
# %% Initialization
import re
from dataclasses import dataclass


@dataclass
class Beacon:
    x: int
    y: int


@dataclass
class Sensor:
    x: int
    y: int
    beacon: Beacon

    @property
    def distance(self):
        return abs(self.x - self.beacon.x) + abs(self.y - self.beacon.y)


def merge_intervals(intervals):
    intervals.sort()

    stack = [intervals.pop(0)]
    for interval in intervals:
        if interval[0] <= stack[-1][1]:
            stack[-1][1] = max(stack[-1][1], interval[1])
        else:
            stack.append(interval)
    return stack


# %% Read input
with open("day_15_input.txt") as data:
    sensors = []
    cleared = set()
    for line in data:
        sx, sy, bx, by = map(int, re.findall(r"-?\d+", line))
        sensors.append(Sensor(sx, sy, Beacon(bx, by)))

# %% Part 1
y = 2000000
intervals = []
for sensor in sensors:
    print("Sensor:", sensor)
    print("  Distance to beacon:", sensor.distance)
    d = abs(sensor.y - y)
    print(f"  Distance to y={y}:", d)
    if sensor.distance >= d:
        remainder = sensor.distance - d
        intervals.append([sensor.x - remainder, sensor.x + remainder])
        print("  Recording interval", intervals[-1])

stack = merge_intervals(intervals)

print("No beacon positions:", sum(abs(a - b) for a, b in stack))


# %% Part 2
for y in range(4_000_000):
    if y % 100_000 == 0:
        print("Processing line", y)
    intervals = []
    for sensor in sensors:
        d = sensor.distance - abs(sensor.y - y)
        if d >= 0:
            intervals.append([sensor.x - d, sensor.x + d])
    if not intervals:
        continue

    stack = merge_intervals(intervals)

    if len(stack) > 1:
        print("Beacon frequency:", y + (stack[0][1]+1) * 4_000_000)
        break

