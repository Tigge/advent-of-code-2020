import functools
import operator


def parse(f):
    return [[set(g2) for g2 in g1.split("\n")] for g1 in f.read().strip().split("\n\n")]


with open("day6.txt", "r", encoding="utf-8") as f:
    groups = list(parse(f))

    p1 = (functools.reduce(operator.or_, group) for group in groups)
    p2 = (functools.reduce(operator.and_, group) for group in groups)

    print(f"Part 1: {sum(map(len, p1))}")
    print(f"Part 2: {sum(map(len, p2))}")
