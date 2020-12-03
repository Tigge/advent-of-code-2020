import itertools
import re


def parse(f):
    d = f.read().strip().split("\n")
    d2 = map(
        lambda l: re.match(r"^(\d+)-(\d+) ([a-z]): (\w+)$", l).groups(),
        d,
    )
    return map(lambda i: (int(i[0]), int(i[1]), i[2], i[3]), d2)


def validate1(min, max, letter, password):
    c = password.count(letter)
    return min <= c <= max


def validate2(a, b, letter, password):
    return password[a - 1] != password[b - 1] and (
        password[a - 1] == letter or password[b - 1] == letter
    )


with open("day2.txt", "r", encoding="utf-8") as f:
    d = list(parse(f))

    print("Part 1:", list(map(lambda i: validate1(*i), d)).count(True))
    print("Part 2:", list(map(lambda i: validate2(*i), d)).count(True))
