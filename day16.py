import itertools
import functools
import operator
import re


def parse(f):

    [fields, my_ticket, nearby_tickets] = f.read().strip().split("\n\n")

    fields = re.findall(
        r"^([\w\s]+): (\d+)-(\d+) or (\d+)-(\d+)$", fields, re.MULTILINE
    )
    fields = list(
        map(lambda r: (r[0], (int(r[1]), int(r[2])), (int(r[3]), int(r[4]))), fields)
    )

    my_ticket = list(map(int, my_ticket.split("\n")[1].split(",")))
    nearby_tickets = list(
        map(lambda row: list(map(int, row.split(","))), nearby_tickets.split("\n")[1:])
    )

    return fields, my_ticket, nearby_tickets


def field_ok(field, number):
    return field[1][0] <= number <= field[1][1] or field[2][0] <= number <= field[2][1]


with open("day16.txt", "r", encoding="utf-8") as f:
    fields, my_ticket, nearby_tickets = parse(f)

    p1 = 0
    nearby_ok_tickets = []
    for ticket in nearby_tickets:
        for n in ticket:
            if any(field_ok(field, n) for field in fields):
                continue
            break
        else:
            nearby_ok_tickets.append(ticket)
            continue
        p1 += n

    print(f"Part 1: {p1}")

    possible = dict()
    for field in fields:
        for i in range(len(fields)):
            if all(field_ok(field, ticket[i]) for ticket in nearby_ok_tickets):
                possible.setdefault(field[0], []).append(i)

    things = sorted(possible.items(), key=lambda i: len(i[1]))

    mapping = {}
    for field, pos in things:
        num = pos[0]
        mapping[field] = num
        for thing in things:
            if num in thing[1]:
                thing[1].remove(num)

    p2 = functools.reduce(
        operator.mul,
        (my_ticket[v] for k, v in mapping.items() if k.startswith("departure")),
    )

    print(f"Part 2: {p2}")
