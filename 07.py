import aoc

crabs = *map(int, aoc.get_input(7).split(",")),

fuels1 = []

for highest_crab in range(max(crabs)):
    fuel_used = sum(abs(crab - highest_crab) for crab in crabs)
    fuels1.append(fuel_used)

fuels2 = []

for highest_crab in range(max(crabs)):
    fuel_used = sum(abs(crab - highest_crab) *
                    (abs(crab - highest_crab) + 1) for crab in crabs) // 2
    fuels2.append(fuel_used)

print("Part 1:", min(fuels1))
print("Part 2:", min(fuels2))
