from pathlib import Path
from time import perf_counter
import math
from itertools import combinations

input_path = Path(__file__).with_suffix(".input")
test_path = Path(__file__).with_suffix(".test")


def iter_lines(file_path):
    with open(file_path) as f:
        for line in f:
            yield line.rstrip("\n")


def solve(file_path, part, test=False):

    solution = 0

    positions = [
        (x, y, z)
        for line in iter_lines(file_path)
        for x, y, z in [map(int, line.split(","))]
    ]

    def sorted_pairs_by_distance(positions):
        pairs = []
        for pos1, pos2 in combinations(range(len(positions)), 2):
            distance = math.dist(positions[pos1], positions[pos2])
            pairs.append((distance, pos1, pos2))
        pairs.sort(key=lambda pair: pair[0])
        return pairs

    def build_circuits(positions, iterations):
        pairs = sorted_pairs_by_distance(positions)
        used_pairs = set()
        circuits = []
        idx = 0

        for step in range(iterations):
            while idx < len(pairs) and (pairs[idx][1], pairs[idx][2]) in used_pairs:
                idx += 1
            if idx >= len(pairs):
                break

            _, pos1, pos2 = pairs[idx]
            idx += 1
            used_pairs.add((pos1, pos2))

            pos1 = positions[pos1]
            pos2 = positions[pos2]

            if len(circuits) == 0:
                circuits = [{pos1, pos2}]
                continue

            found_matching = False
            for circuit in circuits:
                if pos1 in circuit:
                    circuit.add(pos2)
                    found_matching = True
                if pos2 in circuit:
                    circuit.add(pos1)
                    found_matching = True

            if not found_matching:
                circuits.append({pos1, pos2})

        return circuits

    if part == 1:

        iterations = 10 if test else 1000
        circuits = build_circuits(positions, iterations)
        sorted_circuits = sorted(
            circuits, key=lambda circuit: len(circuit), reverse=True
        )

        solution = math.prod([len(circuit) for circuit in sorted_circuits[0:3]])
        return solution

    if part == 2:

        def next_closest_coord(positions: list[tuple]):
            calculations = {}
            total_positions = len(positions)
            for pos1_idx, pos1 in enumerate(positions):
                for pos2 in positions[pos1_idx + 1 : total_positions]:
                    calculations[(pos1, pos2)] = math.dist(pos1, pos2)
            calculations = dict(sorted(calculations.items(), key=lambda item: item[1]))
            for circuit_pair, _ in calculations.items():
                yield circuit_pair

        circuit_membership = {}
        total_positions = len(positions)

        def add_circuit(circuit_pair: tuple[tuple]):
            circuit_id = (
                circuit_membership[max(circuit_membership, key=circuit_membership.get)]
                if circuit_membership
                else 0
            ) + 1
            pos1, pos2 = circuit_pair[0], circuit_pair[1]
            pos1_circuit_id = circuit_membership.get(pos1, None)
            pos2_circuit_id = circuit_membership.get(pos2, None)
            if pos1_circuit_id == pos2_circuit_id != None:
                return False
            circuit_membership[pos1] = circuit_membership[pos2] = circuit_id
            if pos1_circuit_id != pos2_circuit_id:
                new_circuit_members = [
                    pos
                    for pos, circuit_id in circuit_membership.items()
                    if circuit_id in (pos1_circuit_id, pos2_circuit_id)
                ]
                for pos in new_circuit_members:
                    circuit_membership[pos] = circuit_id
            if len(circuit_membership) == total_positions and len(
                set(circuit_membership.values())
            ):
                return True

        circuits_by_distance = next_closest_coord(positions)
        for circuit_pair in circuits_by_distance:
            all_circuits_joined = add_circuit(circuit_pair)
            if all_circuits_joined:
                return circuit_pair[0][0] * circuit_pair[1][0]


for part in [1, 2]:
    start = perf_counter()
    print("❄️ ❄️ ❄️ ❄️ ❄️ ❄️")
    print(f"❄️  Part {part} ❄️ ")
    print("❄️ ❄️ ❄️ ❄️ ❄️ ❄️")
    print("🧪", solve(test_path, part, True))
    print("🎬", solve(input_path, part, False))
    end = perf_counter()
    print("⏰", end - start)
