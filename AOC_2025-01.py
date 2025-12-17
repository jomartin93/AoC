from pathlib import Path
from time import perf_counter

input_file = Path(__file__).with_suffix(".input")
test_file = Path(__file__).with_suffix(".test")


def run(input_file, part):

    if part == 1:

        with open(input_file, "r") as f:
            input = f.read().splitlines()

        code_counter = 0
        current_pos = 50

        for move in input:
            clockwise = 1 if move[0] == "R" else 0
            tick_count = int("".join(move[1:]))
            if clockwise:
                calc = current_pos + tick_count
                while calc > 99:
                    calc = calc - 100
                current_pos = calc
            if not clockwise:
                calc = current_pos - tick_count
                while calc < 0:
                    calc = calc + 100
                current_pos = calc
            if calc == 0:
                code_counter += 1

        return code_counter

    if part == 2:

        with open(input_file, "r") as f:
            lines = f.read().splitlines()

        code_counter = 0
        current_pos = 50

        for move in lines:
            initial_pos = current_pos
            point_count = 0
            direction = 1 if move[0] == "R" else -1
            tick_count = int(move[1:])
            # where we end up before coverting to dial
            calc = current_pos + (direction * tick_count)
            # reliably get position on dial
            current_pos = calc % 100
            # how many times we have "passed" 0 on dial
            wraps = calc // 100
            point_count += abs(wraps)
            # handle starting from 0
            if initial_pos == 0 and wraps < 0:
                point_count -= 1
            # handle ending at 0
            if current_pos == 0 and wraps <= 0:
                point_count += 1
            code_counter += point_count

        return code_counter


for part in [1, 2]:
    print("------")
    print(f"Part {part}")
    print("------")
    start = perf_counter()
    print("  Test: ", run(test_file, part))
    end = perf_counter()
    print("  Time: ", end - start)
    print("  ------")
    start = perf_counter()
    print("  Actual: ", run(input_file, part))
    end = perf_counter()
    print("  Time: ", end - start)
    print("  ------")
