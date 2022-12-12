#  --- Day 11: Monkey in the Middle ---
# %% Initialization
import math
import re
from dataclasses import dataclass


@dataclass
class Monkey:
    items: list[int] = None
    operator: str = ""
    op_value: str = ""
    test_denominator: int = 0
    target_true: int = 0
    target_false: int = 0
    inspections: int = 0

    def operation(self, value):
        second_value = int(self.op_value) if self.op_value.isdigit() else value
        if self.operator == "+":
            return value + second_value
        else:
            return value * second_value

    def inspect_part1(self):
        print(f"  Inspecting item {self.items[0]}")
        print(f"  New worry level is:", self.operation(self.items[0]))
        print(f"  New worry after getting bored:", self.operation(self.items[0]) // 3)

        self.inspections += 1
        return self.operation(self.items.pop(0)) // 3

    def inspect_part2(self):
        print(f"  Inspecting item {self.items[0]}")
        print(f"  New worry level is:", self.operation(self.items[0]))
        self.inspections += 1
        return self.operation(self.items.pop(0)) % magic_modulo

    def test(self, item):
        if item % self.test_denominator == 0:
            print(
                f"  Item {item} is devisible by {self.test_denominator}, tossing to {self.target_true}"
            )
            return self.target_true
        print(
            f"  Item {item} is not devisible by {self.test_denominator}, tossing to {self.target_false}"
        )
        return self.target_false


# %% Read input
monkeys = []
with open("day_11_input.txt") as data:
    while line := data.readline():
        if line.startswith("Monkey"):
            monkey = Monkey()
            for _ in range(5):
                line = data.readline().strip()
                if line.startswith("Starting items:"):
                    monkey.items = [int(x) for x in line.split(":")[1].split(",")]
                elif line.startswith("Operation:"):
                    op, value = re.search(
                        r"new = old (?P<op>.) (?P<value>\d+|\w+)", line
                    ).groups()
                    monkey.operator = op
                    monkey.op_value = value
                elif line.startswith("Test:"):
                    value = re.search(r"(\d+)", line).group(1)
                    monkey.test_denominator = int(value)
                elif line.startswith("If true:"):
                    value = re.search(r"(\d+)", line).group(1)
                    monkey.target_true = int(value)
                elif line.startswith("If false:"):
                    value = re.search(r"(\d+)", line).group(1)
                    monkey.target_false = int(value)
            monkeys.append(monkey)

magic_modulo = math.prod(x.test_denominator for x in monkeys)


# %% Part 1
for i in range(20):
    for j, monkey in enumerate(monkeys):
        print(f"Monkey {j} starts inspections:")
        while monkey.items:
            item = monkey.inspect_part1()
            target = monkey.test(item)
            monkeys[target].items.append(item)
        else:
            print(f"  Monkey {j} holds no (more) items")

print(
    math.prod(x.inspections for x in sorted(monkeys, key=lambda x: x.inspections)[-2:])
)

# %% Part 2
for i in range(10000):
    for j, monkey in enumerate(monkeys):
        while monkey.items:
            item = monkey.inspect_part2()
            target = monkey.test(item)
            monkeys[target].items.append(item)

print(
    math.prod(x.inspections for x in sorted(monkeys, key=lambda x: x.inspections)[-2:])
)
