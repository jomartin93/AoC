from pathlib import Path

input_path = Path(__file__).with_suffix(".input")
test_path = Path(__file__).with_suffix(".test")


def run(file_path, part):
    with open(file_path, "r") as file:
        rows = file.read().splitlines()

    rows = [[i for i in row] for row in rows]
    rolls_of_paper = 0
    width = len(rows[0])
    height = len(rows)

    if part == 1:
        for row in range(height):
            for col in range(width):
                adjacent = []
                if rows[row][col] != "@":
                    continue
                for dr_vert in [-1, 0, 1]:
                    if row + dr_vert < 0:
                        continue
                    if row + dr_vert >= height:
                        continue
                    for dr_horz in [-1, 0, 1]:
                        if dr_vert == 0 and dr_horz == 0:
                            continue
                        if col + dr_horz < 0:
                            continue
                        if col + dr_horz >= width:
                            continue
                        adjacent.append(rows[row + dr_vert][col + dr_horz])
                if adjacent.count("@") < 4:
                    rolls_of_paper += 1

    if part == 2:

        def remove_rolls(rows, total):
            pos_to_replace = []
            for row in range(height):
                for col in range(width):
                    adjacent = []
                    if rows[row][col] != "@":
                        continue
                    for dr_vert in [-1, 0, 1]:
                        if row + dr_vert < 0:
                            continue
                        if row + dr_vert >= height:
                            continue
                        for dr_horz in [-1, 0, 1]:
                            if dr_vert == 0 and dr_horz == 0:
                                continue
                            if col + dr_horz < 0:
                                continue
                            if col + dr_horz >= width:
                                continue
                            adjacent.append(rows[row + dr_vert][col + dr_horz])
                    if adjacent.count("@") < 4:
                        pos_to_replace.append([row, col])
                        total += 1

            if len(pos_to_replace) == 0:
                return True, rows, total

            for pos in pos_to_replace:
                rows[pos[0]][pos[1]] = "."

            return False, rows, total

        complete = False
        while not complete:
            complete, rows, rolls_of_paper = remove_rolls(rows, rolls_of_paper)

    return rolls_of_paper


def revised(file_path, part):
    with open(file_path) as f:
        rows = f.read().splitlines()

    remaining_rolls = {
        (y, x)
        for y, row in enumerate(rows)
        for x, char in enumerate(row)
        if char == "@"
    }

    rolls_removed = 0

    if part == 1:
        for y, x in remaining_rolls:
            adjacent = 0
            for dr_x in [-1, 0, 1]:
                for dr_y in [-1, 0, 1]:
                    if dr_x == dr_y == 0:
                        continue
                    if (y + dr_y, x + dr_x) in remaining_rolls:
                        adjacent += 1
            if adjacent < 4:
                rolls_removed += 1

    if part == 2:

        valid_rolls = True

        while valid_rolls:
            roll_removed = False
            rolls_to_remove = []
            for y, x in remaining_rolls:
                adjacent = 0
                for dr_y in [-1, 0, 1]:
                    for dr_x in [-1, 0, 1]:
                        if dr_y == dr_x == 0:
                            continue
                        if (y + dr_y, x + dr_x) in remaining_rolls:
                            adjacent += 1
                if adjacent < 4:
                    rolls_to_remove.append((y, x))
                    roll_removed = True
                    rolls_removed += 1
            for roll in rolls_to_remove:
                remaining_rolls.remove(roll)
            if not roll_removed:
                valid_rolls = False

    return rolls_removed


for part in [1, 2]:
    # part 1: 31m
    # part 2: 1h16m (45m)
    print("------")
    print(f"Part {part}")
    print("------")
    print("  Test:", run(test_path, part))
    print("  Revised:", revised(test_path, part))
    print("  ------")
    print("  Actual:", run(input_path, part))
    print("  Revised:", revised(input_path, part))
