import itertools
import functools
import operator
import re


def parse(f):
    return list(map(int, f.read().strip().split("\n")))


def part1(numbers):
    i = 25
    while i < len(numbers):
        preamble = numbers[i - 25 : i]
        if numbers[i] not in set(
            map(lambda a: a[0] + a[1], itertools.combinations(preamble, 2))
        ):
            return numbers[i]
        i += 1


def part2(numbers, bad):
    for i, v1 in enumerate(numbers):
        mi, ma, s = v1, v1, v1
        for v2 in numbers[i + 1 :]:
            s += v2
            mi, ma = min(mi, v2), max(ma, v2)
            if s == bad:
                return mi + ma


with open("day9.txt", "r", encoding="utf-8") as f:
    numbers = parse(f)

    bad = part1(numbers)
    weakness = part2(numbers, bad)

    print(f"Part 1: {bad}")
    print(f"Part 2: {weakness}")
