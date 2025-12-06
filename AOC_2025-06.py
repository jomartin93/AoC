from pathlib import Path
from time import perf_counter
import re
import math

input_path = Path(__file__).with_suffix(".input")
test_path = Path(__file__).with_suffix(".test")


def solve(file_path, part):

    total = 0

    if part == 1:
        with open(file_path, "r") as file:
            lines = file.read().splitlines()

        grid = [re.findall(r"\S+", line) for line in lines]
        columns = zip(*grid)

        for *number_str, op in columns:
            values = [int(number) for number in number_str]
            if op == "*":
                total += math.prod(values)
            else:
                total += sum(values)

    if part == 2:
        with open(file_path, "r") as file:
            grid = [list(line.rstrip("\n")) for line in file]

        place_value_grid = zip(*grid)
        current = 0
        op = ""

        for column in place_value_grid:
            if not any(char.isdigit() for char in column):
                total += current
                current = 0
                op = ""
                continue

            if column[-1] in ["*", "+"]:
                op = column[-1]
                current = 1 if op == "*" else 0

            value = int("".join(column[:-1]).strip())
            if op == "*":
                current *= value
            else:
                current += value

        total += current

    return total


for part in [1, 2]:
    start = perf_counter()
    print("------")
    print(f"Part {part}")
    print("------")
    print("  Test:", solve(test_path, part))
    print("  Actual:", solve(input_path, part))
    end = perf_counter()
    print("  Total Time: ", end - start)
    print("  ------")
