import itertools
import functools
import operator


def parse(f):
    [num, rest] = f.read().strip().split("\n")
    return (int(num), [int(x) if x != "x" else None for x in rest.split(",")])


def p1(busses, time):
    valid_busses = [b for b in busses if b is not None]
    offset_busses = [b - time % b for b in valid_busses]
    return valid_busses[offset_busses.index(min(offset_busses))] * min(offset_busses)


def p2(busses):
    bus_offsets = zip(busses, itertools.count())
    bus_offsets = list(filter(lambda x: x[0] != None, bus_offsets))

    start = bus_offsets[0][0]
    period = 1
    for v in bus_offsets:
        for j in range(start, period * v[0], period):
            if (j + v[1]) % v[0] == 0:
                start = j
                break
        period *= v[0]
    return start


with open("day13.txt", "r", encoding="utf-8") as f:
    [time, busses] = parse(f)

    print(f"Part 1: {p1(busses, time)}")
    print(f"Part 2: {p2(busses)}")
