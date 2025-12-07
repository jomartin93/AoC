import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-p", "--part", type=int, choices=[1, 2], required=True)
args = parser.parse_args()

PART = args.part

# SECTION Part 1: Original
if PART == 1:
    from pathlib import Path

    # initial, perhaps dump way
    # import re
    # file = re.search(r"([^\//]*)$", __file__).group(1).replace(".py", ".input")

    # more pythonic
    input_file = Path(__file__).stem + ".input"

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

    print(code_counter)

# !SECTION
# SECTION ChatGPT

# from pathlib import Path

# # load input
# input_file = Path(__file__).with_suffix(".input")

# with open(input_file, "r") as f:
#     lines = f.read().splitlines()

# code_counter = 0
# current_pos = 50

# for move in lines:
#     direction = 1 if move[0] == "R" else -1
#     tick_count = int(move[1:])

#     current_pos = (current_pos + direction * tick_count) % 100

#     if current_pos == 0:
#         code_counter += 1

# print(code_counter)
# !SECTION
# SECTION Part 2: Building of Part 1 ChatGPT
elif PART == 2:

    from pathlib import Path

    input_file = Path(__file__).with_suffix(".input")

    with open(input_file, "r") as f:
        lines = f.read().splitlines()

    code_counter = 0
    current_pos = 50

    SAMPLE = [
        "L68",
        "L30",
        "R48",
        "L5",
        "R60",
        "L55",
        "L1",
        "L99",
        "R14",
        "L82",
    ]
    # lines = SAMPLE

    for move in lines:
        initial_pos = current_pos
        # print(initial_pos)
        # print(move)
        point_count = 0
        direction = 1 if move[0] == "R" else -1
        tick_count = int(move[1:])
        # where we end up before coverting to dial
        calc = current_pos + (direction * tick_count)
        # reliably get position on dial
        current_pos = calc % 100
        # print(current_pos)
        # how many times we have "passed" 0 on dial
        wraps = calc // 100
        # handle starting from 0
        point_count += abs(wraps)
        if initial_pos == 0 and wraps < 0:
            point_count += -1
        # handle ending at 0
        if current_pos == 0 and wraps <= 0:
            point_count += 1
        # print(point_count)
        code_counter += point_count
        # print(code_counter)
        # if current_pos == 0:
        #     print("final on 0")
        #     code_counter += 1
        # print(code_counter)
        # break
        # print(code_counter)

    print(code_counter)
# !SECTION
# SECTION Building off my original
# if PART == 2:
#     from pathlib import Path

#     input_file = Path(__file__).stem + ".input"

#     with open(input_file, "r") as f:
#         input = f.read().splitlines()

#     code_counter = 0
#     current_pos = 50

#     SAMPLE = [
#         "L68",
#         "L30",
#         "R48",
#         "L5",
#         "R60",
#         "L55",
#         "L1",
#         "L99",
#         "R14",
#         "L82",
#     ]
#     input = SAMPLE

#     for move in input:
#         print(move)
#         clockwise = 1 if move[0] == "R" else 0
#         tick_count = int("".join(move[1:]))
#         if clockwise:
#             calc = current_pos + tick_count
#             while calc > 99:
#                 calc = calc - 100
#                 if not calc == 0:
#                     code_counter += 1
#             current_pos = calc
#         if not clockwise:
#             calc = current_pos - tick_count
#             while calc < 0:
#                 calc = calc + 100
#                 if not calc == 0 and not current_pos == 0:
#                     code_counter += 1
#             current_pos = calc
#         if calc == 0:
#             code_counter += 1
#         print(current_pos)
#         print(code_counter)

#     print(code_counter)

# !SECTION
