import itertools
import functools
import operator
import re


def parse(f):
    return [
        list(filter(lambda x: x != " ", list(line)))
        for line in f.read().strip().split("\n")
    ]


def process(expression, i=0, level=0):
    stack = [[]]
    while i < len(expression):
        token = expression[i]

        if token == "(":
            stack.append([])
        elif token == ")":
            s = stack.pop()
            stack[-1].append(("par", s))
        elif token in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            stack[-1].append(("num", int(token)))
        else:
            stack[-1].append(("op", token))
        i += 1
    return stack[0]


def do(thing):
    (op, rest) = thing

    if op == "num":
        return rest

    if op == "par":
        prev = None
        i = 0
        while i < len(rest):

            thing = rest[i]
            if thing[0] == "op":
                if thing[1] == "+":
                    prev = prev + do(rest[i + 1])
                if thing[1] == "*":
                    prev = prev * do(rest[i + 1])
                i += 1
            else:
                prev = do(thing)
            i += 1
        return prev


def do2(thing):
    (op, rest) = thing

    if op == "num":
        return rest

    if op == "par":
        i = 0
        while i < len(rest):

            thing = rest[i]
            if thing[0] == "op":
                if thing[1] == "+":
                    prev = do2(rest[i - 1]) + do2(rest[i + 1])
                    rest = rest[0 : i - 1] + [("num", prev)] + rest[i + 2 :]
                    continue
            i += 1

        i = 0
        while i < len(rest):

            thing = rest[i]
            if thing[0] == "op":
                if thing[1] == "*":
                    prev = do2(rest[i - 1]) * do2(rest[i + 1])
                    rest = rest[0 : i - 1] + [("num", prev)] + rest[i + 2 :]
                    continue
            i += 1

        return rest[0][1]


with open("day18.txt", "r", encoding="utf-8") as f:
    lines = parse(f)

    p = process(lines[0])

    p1 = sum([do(("par", process(line))) for line in lines])
    p2 = sum([do2(("par", process(line))) for line in lines])

    print(f"Part 1: {p1}")
    print(f"Part 2: {p2}")