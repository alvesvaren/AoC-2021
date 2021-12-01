from aoc import get_input

data = *map(int, get_input(1).splitlines()),

def calculate_larger(data):
    count = 0
    last_item = None
    for item in data:
        if last_item is not None and item > last_item:
            count += 1
        last_item = item
    return count

new_data = []

for first, second, third in zip(data, data[1:], data[2:]):
    new_data.append(first + second + third)



print("Part 1:", calculate_larger(data))
print("Part 2:", calculate_larger(new_data))
