import itertools


def find2(numbers):
    for a, b in itertools.combinations(numbers, 2):
        if a + b == 2020:
            return a * b


def find3(numbers):
    for a, b, c in itertools.combinations(numbers, 3):
        if a + b + c == 2020:
            return a * b * c


def parse(f):
    return map(lambda l: int(l), f.readlines())


with open("day1.txt", "r", encoding="utf-8") as f:
    d = list(parse(f))
    print("Part 1:", find2(d))
    print("Part 2:", find3(d))
