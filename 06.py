import aoc
from collections import defaultdict

fishes = list(map(int, aoc.get_input(6).split(",")))

def count_fishes(fishes: list[int], days: int):
    fishes_for_days = {8: 0, 7: 0, 6: 0, 5: 0, 4: 0, 3: 0, 2: 0, 1: 0, 0: 0}

    for fish in fishes:
        fishes_for_days[fish] += 1

    for _ in range(days):
        start_fishes = fishes_for_days.copy()
        fishes_for_days[8] += fishes_for_days[0]
        fishes_for_days[6] += fishes_for_days[0]
        fishes_for_days[0] = 0
        for fish, count in start_fishes.items():
            if count == 0 or fish == 0:
                continue
            fishes_for_days[fish] -= count
            fishes_for_days[fish - 1] += count

    return sum(fishes_for_days.values())


print("Part 1:", count_fishes(fishes, 80))
print("Part 2:", count_fishes(fishes, 256))
