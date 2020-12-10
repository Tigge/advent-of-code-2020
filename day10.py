def parse(f):
    return sorted(list(map(int, f.read().strip().split("\n"))))


def counts(adapters):
    diffs = {1: 0, 2: 0, 3: 0}
    for a1, a2 in zip([0] + adapters, adapters + [adapters[-1] + 3]):
        diffs[a2 - a1] += 1
    return diffs


def combinations(adapters):
    amounts = {**{a: 0 for a in adapters}, adapters[-1]: 1}
    for a in reversed(list(adapters)):
        for r in [1, 2, 3]:
            amounts[a] += amounts.get(a + r, 0)
    return amounts


with open("day10.txt", "r", encoding="utf-8") as f:
    adapters = parse(f)

    p1 = counts(adapters)
    p2 = combinations([0] + adapters + [adapters[-1] + 3])

    print(f"Part 1: {p1[1] * p1[3]}")
    print(f"Part 2: {p2[0]}")
