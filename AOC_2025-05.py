from pathlib import Path
from time import perf_counter

input_path = Path(__file__).with_suffix(".input")
test_path = Path(__file__).with_suffix(".test")


def run(file_path, part):
    with open(file_path, "r") as file:
        data = file.read().splitlines()

    fresh = 0

    if part == 1:
        fresh_ranges, ingredient_start = get_fresh_ranges(data)

        for line in range(ingredient_start, len(data)):
            ingredient = int(data[line])
            for fresh_range in fresh_ranges:
                if fresh_range[0] <= ingredient <= fresh_range[1]:
                    fresh += 1
                    break

    if part == 2:
        possible_fresh = []
        fresh_ranges, _ = get_fresh_ranges(data)
        fresh_ranges = sorted(fresh_ranges, key=lambda fresh_range: fresh_range[0])
        pos = 0
        for fresh_range in fresh_ranges:
            if len(possible_fresh) == 0:
                possible_fresh.append(fresh_range)
            old_min = possible_fresh[pos][0]
            old_max = possible_fresh[pos][1]
            new_min = fresh_range[0]
            new_max = fresh_range[1]
            if old_min <= new_min <= old_max + 1:
                if old_max >= new_max:
                    continue
                if old_max < new_max:
                    # this is ugly, but old_max didn't point to list I want to modify
                    possible_fresh[pos][1] = new_max
            if old_max + 1 < new_min:
                possible_fresh.append(fresh_range)
                pos += 1
        for fresh_range in possible_fresh:
            fresh += fresh_range[1] - fresh_range[0] + 1

    return fresh


def revised(file_path, part):
    with open(file_path, "r") as file:
        data = file.read().splitlines()

    fresh = 0

    if part == 1:
        fresh_ranges, ingredient_start = get_fresh_ranges(data)
        fresh_ranges = clean_ranges(fresh_ranges)
        for line in range(ingredient_start, len(data)):
            ingredient = int(data[line])
            for fresh_range in fresh_ranges:
                if fresh_range[0] <= ingredient <= fresh_range[1]:
                    fresh += 1
                    break
    if part == 2:
        fresh_ranges, _ = get_fresh_ranges(data)
        fresh_ranges = clean_ranges(fresh_ranges)
        for fresh_range in fresh_ranges:
            fresh += fresh_range[1] - fresh_range[0] + 1

    return fresh


def get_fresh_ranges(data):
    fresh_ranges = []
    for line in range(len(data)):
        try:
            fresh_range = list(map(int, str(data[line]).split("-")))
            # when we hit the blank line, ValueError is raised
        except ValueError:
            ingredient_start = line + 1
            break
        fresh_ranges.append(fresh_range)
    return fresh_ranges, ingredient_start


def clean_ranges(ranges):
    possible_fresh = []
    fresh_ranges = sorted(ranges, key=lambda fresh_range: fresh_range[0])
    pos = 0
    for fresh_range in fresh_ranges:
        if len(possible_fresh) == 0:
            possible_fresh.append(fresh_range)
        old_min = possible_fresh[pos][0]
        old_max = possible_fresh[pos][1]
        new_min = fresh_range[0]
        new_max = fresh_range[1]
        if old_min <= new_min <= old_max + 1:
            if old_max >= new_max:
                continue
            if old_max < new_max:
                # this is ugly, but old_max didn't point to list I want to modify
                possible_fresh[pos][1] = new_max
        if old_max + 1 < new_min:
            possible_fresh.append(fresh_range)
            pos += 1
    return possible_fresh


for part in [1, 2]:
    start = perf_counter()
    print("------")
    print(f"Part {part}")
    print("------")
    print("  Test:", run(test_path, part))
    print("  Actual:", run(input_path, part))
    end = perf_counter()
    print("  Total Time: ", end - start)
    print("  ------")
    start = perf_counter()
    print("  Revised Test:", revised(test_path, part))
    print("  Revised Actual:", revised(input_path, part))
    end = perf_counter()
    print("  Total Time: ", end - start)
    print("------")
