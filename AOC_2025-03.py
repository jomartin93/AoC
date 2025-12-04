from pathlib import Path

input_path = Path(__file__).with_suffix(".input")
test_path = Path(__file__).with_suffix(".test")


def run(file_path, part):
    with open(file_path, "r") as file:
        lines_list = file.read().splitlines()

    banks = [str(bank) for bank in lines_list]
    jolt_sum = 0

    if part == 1:
        for bank in banks:
            bank_len = len(bank)
            max_jolts = 0
            for bat_idx in range(bank_len):
                if bat_idx == bank_len - 1:
                    break
                bat = int(bank[bat_idx])
                if bat < int(str(max_jolts)[0]):
                    continue
                for bat2_idx in range(bat_idx + 1, bank_len):
                    bat_pair = int(str(bat) + (bank[bat2_idx]))
                    max_jolts = max(max_jolts, bat_pair)
            jolt_sum += max_jolts

    elif part == 2:
        for bank in banks:
            bank_len = len(bank)
            jolt_build = ""
            for bat_idx in range(bank_len):
                bat = bank[bat_idx]
                bats_needed = 12 - len(jolt_build)
                remaining_bats = bank_len - bat_idx
                if bats_needed > remaining_bats:
                    break
                valid_bats = bank[bat_idx : bank_len - bats_needed + 1]
                next_max = max([int(b) for b in valid_bats])
                if int(bat) == next_max:
                    jolt_build += bat
                if len(jolt_build) == 12:
                    break
            jolt_sum += int(jolt_build)

    return jolt_sum


for part in [1, 2]:
    print("------")
    print(f"Part {part}")
    print("------")
    print("  Test:", run(test_path, part))
    print("  ------")
    print("  Actual:", run(input_path, part))
