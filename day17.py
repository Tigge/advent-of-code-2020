import itertools
import functools
import operator
import re


def parse(f):
    active = []
    for y, l in enumerate(f.read().strip().split("\n")):
        for x, i in enumerate(l):
            if i == "#":
                active.append((x, y))
    return active


def find_neighbours(cubes):
    neighbours = dict()

    for cube in cubes:
        for offset in itertools.product([-1, 0, 1], repeat=len(cube)):
            c = tuple(map(operator.add, cube, offset))
            if c != cube:
                neighbours[c] = neighbours.setdefault(c, 0) + 1

    return neighbours


def step(cubes):
    neighbours = find_neighbours(cubes)
    next_cubes = []

    for cube, neighbour in neighbours.items():
        active = cube in cubes

        if (active and (neighbour == 2 or neighbour == 3)) or (
            not active and neighbour == 3
        ):
            next_cubes.append(cube)

    return next_cubes


def process(cubes):
    for _ in range(0, 6):
        cubes = step(cubes)
    return cubes


with open("day17.txt", "r", encoding="utf-8") as f:
    cubes = parse(f)

    print(f"Part 1: {len(process([(*c, 0) for c in cubes]))}")
    print(f"Part 2: {len(process([(*c, 0, 0) for c in cubes]))}")