import functools
import operator


def parse(f):
    return f.read().strip().split("\n")


def slope(field, right, down):
    width, height = len(field[0]), len(field)
    (x, y) = 0, 0
    trees = 0
    while y < height:
        trees += 1 if field[y][x] == "#" else 0
        x = (x + right) % width
        y = y + down

    return trees


with open("day3.txt", "r", encoding="utf-8") as f:
    field = list(parse(f))

    answers = [
        slope(field, 1, 1),
        slope(field, 3, 1),
        slope(field, 5, 1),
        slope(field, 7, 1),
        slope(field, 1, 2),
    ]

    print("Part 1:", answers[1])
    print("Part 2:", functools.reduce(operator.mul, answers))
