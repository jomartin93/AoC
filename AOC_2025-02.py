from pathlib import Path
from time import perf_counter
import re

input_file = Path(__file__).with_suffix(".input")
test_file = Path(__file__).with_suffix(".test")


def run(input_file, part):
    with open(input_file) as f:
        id_file = f.read().strip()

    id_list = [id.split("-") for id in id_file.split(",")]

    def is_repeated(id, part):
        id = str(id)
        id_len = len(id)
        if id_len < 2:
            return False
        if part == 1:
            if id_len % 2 > 0:
                return False
            seg_len = id_len // 2
            s1 = id[0:seg_len]
            s2 = id[seg_len : seg_len * 2]
            if s1 == s2:
                return True
            return False
        elif part == 2:
            for seg_len in range(1, (id_len // 2) + 1):
                # length must be divisible by segment
                if id_len % seg_len > 0:
                    continue
                # first two segments should match
                s1 = id[0:seg_len]
                s2 = id[seg_len : seg_len * 2]
                if s1 == s2:
                    total_segs = id_len // seg_len
                    if total_segs == 2:
                        return True
                    broken_pattern = False
                    # start at the third segment
                    for seg_num in range(2, total_segs):
                        seg = id[seg_len * seg_num : seg_len * seg_num + seg_len]
                        if seg != s1:
                            broken_pattern = True
                            break
                    if not broken_pattern:
                        return True
                continue
            return False

    sum = 0

    for full_id in id_list:
        for inc in range(int(full_id[0]), int(full_id[1]) + 1):
            if is_repeated(inc, part):
                sum += int(inc)

    return sum


def regex(input_file, part):
    with open(input_file) as f:
        id_file = f.read().strip()

    id_list = [id.split("-") for id in id_file.split(",")]

    def is_repeated(id, part):
        id = str(id)
        if part == 1:
            if re.match(r"^(.+?)\1$", id):
                return True
        if part == 2:
            if re.match(r"^(.+?)\1+$", id):
                return True

    sum = 0

    for full_id in id_list:
        for inc in range(int(full_id[0]), int(full_id[1]) + 1):
            if is_repeated(inc, part):
                sum += int(inc)

    return sum


for part in [1, 2]:
    print(f"Part {part}:")
    start = perf_counter()
    print("Test: ", run(test_file, part))
    end = perf_counter()
    print("Time: " + str(end - start))
    start = perf_counter()
    print("Actual: ", run(input_file, part))
    end = perf_counter()
    print("Time: " + str(end - start))
    start = perf_counter()
    print("Regex: ", regex(input_file, part))
    end = perf_counter()
    print("Time: " + str(end - start))
