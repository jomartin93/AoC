from pathlib import Path
from time import perf_counter

input_path = Path(__file__).with_suffix(".input")
test_path = Path(__file__).with_suffix(".test")


def iter_lines(file_path):
    with open(file_path) as f:
        for line in f:
            yield line.rstrip("\n")


def solve(file_path, part):

    solution = 0

    if part == 1:

        lines = iter_lines(file_path)
        beam_splits = 0
        prev_beams = {next(lines).index("S")}

        for line in lines:

            width = len(line)
            curr_beams = set()

            for col in prev_beams:

                if line[col] == "^":
                    for neighbor in (col - 1, col + 1):
                        if 0 <= neighbor < width:
                            curr_beams.add(neighbor)
                    beam_splits += 1

                else:
                    curr_beams.add(col)

            prev_beams = curr_beams

        solution = beam_splits

    if part == 2:

        lines = iter_lines(file_path)
        early_exits = 0
        prev_beams = {next(lines).index("S"): 1}

        for line in lines:

            width = len(line)
            curr_beams = {}

            for col, paths_count in prev_beams.items():

                if line[col] == "^":

                    for neighbor in (col - 1, col + 1):
                        if 0 <= neighbor < width:
                            curr_paths_count = curr_beams.get(neighbor, 0)
                            curr_beams[neighbor] = paths_count + curr_paths_count
                        else:
                            early_exits += prev_beams[col]

                else:
                    curr_beams[col] = curr_beams.get(col, 0) + paths_count

            prev_beams = curr_beams

        solution = sum(prev_beams.values()) + early_exits

    return solution


for part in [1, 2]:
    start = perf_counter()
    print("❄️ ❄️ ❄️ ❄️ ❄️ ❄️")
    print(f"❄️  Part {part} ❄️ ")
    print("❄️ ❄️ ❄️ ❄️ ❄️ ❄️")
    print("🧪", solve(test_path, part))
    print("🎬", solve(input_path, part))
    end = perf_counter()
    print("⏰", end - start)
