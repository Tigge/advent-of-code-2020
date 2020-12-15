import itertools


def parse(f):
    return list(map(int, f.read().strip().split(",")))


def process(numbers):
    result = None
    prev = dict(zip(numbers, itertools.count(start=1)))
    next_number = 0
    for turn in itertools.count(start=len(numbers) + 1):
        current_number = next_number
        if turn == 2020:
            result = current_number

        if turn == 30000000:
            result = (result, current_number)
            break

        if next_number in prev:
            prev_turn = prev[current_number]
            next_number = turn - prev_turn
        else:
            next_number = 0

        prev[current_number] = turn
    return result


with open("day15.txt", "r", encoding="utf-8") as f:
    numbers = parse(f)
    p1, p2 = process(numbers)

    print(f"Part 1: {p1}")
    print(f"Part 2: {p2}")
