import aoc

data = aoc.get_input(3).splitlines()
width = len(data[0])
height = len(data)

num = []


rotated_data = list(zip(*data[::-1]))

for i, column in enumerate(rotated_data):
    ints = *map(int, column),
    average = sum(ints) / height
    num.append(round(average))


def search(_data: list[str], i: int, keep_lower: bool):
    column = list(zip(*_data[::-1]))[i]
    ints = *map(int, column),
    average = sum(ints) / len(_data)
    if average == 0.5:
        average = 1
    val = round(average)

    if keep_lower:
        val = 0 if val == 1 else 1

    kept = [row for row in _data if int(row[i]) == val]
    if len(kept) != 1:
        kept = search(kept, i+1, keep_lower)

    return kept


o2 = int(search(data, 0, False)[0], 2)
co2 = int(search(data, 0, True)[0], 2)


gamma = int("".join((map(str, num))), 2)
elipson = int("".join((map(str, num))), 2) ^ int('0b' + '1' * width, 2)


print("Part 1:", gamma * elipson)
print("Part 2:", o2 * co2)
