import functools
import operator
import re


def parse(f):
    def parse_item(i):
        [bag, rest] = i.split(" bags contain ")
        return bag, list(
            map(lambda b: (b[1], int(b[0])), re.findall(r"([0-9]+) (\w+ \w+)", rest))
        )

    return list(map(parse_item, f.read().strip().split("\n")))


def parse1(o, i):
    bag, bags = i
    o.setdefault(bag, [])
    for b, num in bags:
        o.setdefault(b, []).append((bag, num))
    return o


def parse2(o, i):
    bag, bags = i
    o[bag] = []
    for b, num in bags:
        o[bag].append((b, num))
    return o


def traverse1(bags, bag):
    r = set()
    for b in bags[bag]:
        r |= set([b[0]]) | traverse1(bags, b[0])
    return r


def traverse2(bags, bag):
    return 1 + sum(map(lambda b: b[1] * traverse2(bags, b[0]), bags[bag]))


with open("day7.txt", "r", encoding="utf-8") as f:
    bags = parse(f)

    d1 = functools.reduce(parse1, bags, dict())
    d2 = functools.reduce(parse2, bags, dict())

    print(f"Part 1: {len(traverse1(d1, 'shiny gold'))}")
    print(f"Part 2: {traverse2(d2, 'shiny gold') - 1}")
