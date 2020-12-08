import functools
import operator
import re


def parse(f):
    return list(map(lambda i: (i[0:3], int(i[4:])), f.read().strip().split("\n")))


def run(program):
    pc = 0
    acc = 0
    visited = set()

    while pc < len(program):
        op, val = program[pc]
        if pc in visited:
            return ("err", acc)
        visited |= {pc}

        if op == "acc":
            acc += val
            pc += 1
        elif op == "jmp":
            pc += val
        elif op == "nop":
            pc += 1
    return ("ok", acc)


def debug(program):
    for i, n in enumerate(program):
        if n[0] == "jmp":
            tmp_program = program[:]
            tmp_program[i] = ("nop", tmp_program[i][1])
            res, val = run(tmp_program)
            if res == "ok":
                return val


with open("day8.txt", "r", encoding="utf-8") as f:
    program = parse(f)

    print(f"Part 1: {run(program)[1]}")
    print(f"Part 2: {debug(program)}")
