import itertools
import functools
import operator


def parse(f):
    def parse_item(i):
        [p1, p2] = i.split(" = ")
        if p1.startswith("mask"):
            return ("mask", p2)
        else:
            return ("mem", int(p1[4:-1]), int(p2))

    return list(map(parse_item, f.read().strip().split("\n")))


def apply_mask(mask, number):
    b = list(format(number, "036b"))

    for i, v in enumerate(mask):
        if v != "X":
            b[i] = v

    return int("".join(b), 2)


def apply_mask2(mask, number):
    b = format(number, "036b")

    def thing(i, acc):
        if i == len(mask):
            yield int(acc, 2)
            return

        if mask[i] == "0":
            yield from thing(i + 1, acc + b[i])
        elif mask[i] == "1":
            yield from thing(i + 1, acc + "1")
        else:
            yield from thing(i + 1, acc + "0")
            yield from thing(i + 1, acc + "1")

    yield from thing(0, "")


def p1(instructions):
    mask = None
    mem = dict()
    for i in instructions:
        if i[0] == "mask":
            mask = i[1]
        else:
            mem[i[1]] = apply_mask(mask, i[2])

    return sum(mem.values())


def p2(instructions):
    mask = None
    mem = dict()
    for i in instructions:
        if i[0] == "mask":
            mask = i[1]
        else:
            for addr in apply_mask2(mask, i[1]):
                mem[addr] = i[2]
    return sum(mem.values())


with open("day14.txt", "r", encoding="utf-8") as f:
    instructions = parse(f)

    print(f"Part 1: {p1(instructions)}")
    print(f"Part 2: {p2(instructions)}")
