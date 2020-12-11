import copy
import itertools

MAP = {"L": 0, "#": 1, ".": 0}
DIRS = [(-1, -1), (0, -1), (1, -1), (-1, 0), (1, 0), (-1, 1), (0, 1), (1, 1)]


def parse(f):
    return list(map(list, f.read().strip().split("\n")))


def get_seat(x, y, seats):
    return (
        seats[y][x]
        if y >= 0 and y < len(seats) and x >= 0 and x < len(seats[0])
        else "L"
    )


def get_seat_adj(x, y, dir, seats):
    return get_seat(x + dir[0], y + dir[1], seats)


def get_seat_dir(x, y, dir, seats):
    for i in itertools.count(start=1):
        s = get_seat(x + dir[0] * i, y + dir[1] * i, seats)
        if s == ".":
            continue
        return s


def occupied_seats(x, y, seats, adj):
    return sum(MAP[adj(x, y, dir, seats)] for dir in DIRS)


def next_seats(seats, adj, adjc):
    seats_next = copy.deepcopy(seats)
    for y, row in enumerate(seats):
        for x, _ in enumerate(row):
            n = occupied_seats(x, y, seats, adj)
            if seats[y][x] == "L" and n == 0:
                seats_next[y][x] = "#"
            elif seats[y][x] == "#" and n >= adjc:
                seats_next[y][x] = "L"

    return seats_next


def to_string(seats):
    return "\n".join(map(lambda l: "".join(l), seats))


def process(seats, adj, adjc):
    before, after = None, to_string(seats)
    while before != after:
        before = after
        after = to_string(seats := next_seats(seats, adj, adjc))
    return to_string(seats).count("#")


with open("day11.txt", "r", encoding="utf-8") as f:
    seats = parse(f)

    p1 = process(seats, get_seat_adj, 4)
    p2 = process(seats, get_seat_dir, 5)

    print(f"Part 1: {p1}")
    print(f"Part 2: {p2}")
