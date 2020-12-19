def parse_rule(r):
    if " | " in r:
        [a, b] = r.split(" | ")
        return ("OR", (parse_rule(a), parse_rule(b)))
    elif r.startswith('"'):
        return ("CHAR", r[1])
    else:
        return ("SEQ", [int(t) for t in r.split(" ")])


def parse(f):
    [rules, messages] = f.read().strip().split("\n\n")
    r = dict(
        [
            (int(n), parse_rule(rule))
            for [n, rule] in [rule.split(": ") for rule in rules.split("\n")]
        ]
    )
    return (r, messages.split("\n"))


def matches(rules, rule, message, i):
    if i == len(message):
        return

    (op, rest) = rule

    if op == "CHAR":
        if message[i] == rest:
            yield i + 1
    elif op == "SEQ":
        viable_is = set([i])
        for r in rest:
            next_viable_is = set()
            for i in viable_is:
                next_viable_is |= set(matches(rules, rules[r], message, i))
            viable_is = next_viable_is
        yield from viable_is
    elif op == "OR":
        yield from matches(rules, rest[0], message, i)
        yield from matches(rules, rest[1], message, i)


with open("day19.txt", "r", encoding="utf-8") as f:
    (rules, messages) = parse(f)

    p1 = 0
    for m in messages:
        if len(m) in matches(rules, rules[0], m, 0):
            p1 += 1

    print(f"Part 1: {p1}")

    rules[8] = ("OR", (("SEQ", [42]), ("SEQ", [42, 8])))
    rules[11] = ("OR", (("SEQ", [42, 31]), ("SEQ", [42, 11, 31])))

    p2 = 0
    for m in messages:
        if len(m) in matches(rules, rules[0], m, 0):
            p2 += 1

    print(f"Part 2: {p2}")