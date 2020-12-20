import copy
import math


def rotate(data):
    return ["".join(line) for line in zip(*data[::-1])]


def flip(data):
    return ["".join(line[::-1]) for line in data]


def draw(data):
    for line in data:
        print("".join(line))
    print()


def possible(data):
    for _ in range(4):
        yield data
        yield flip(data)
        data = rotate(data)


def count(data):
    return sum([line.count("#") for line in data])


SNEK = [
    "                  # ",
    "#    ##    ##    ###",
    " #  #  #  #  #  #   ",
]


def count_snek(data):
    sneks = 0
    for y, line in enumerate(data):
        for x, _ in enumerate(line):
            try:
                for sy, sline in enumerate(SNEK):
                    for sx, schar in enumerate(sline):
                        if schar == "#" and data[y + sy][x + sx] != "#":
                            break
                    else:
                        continue
                    break
                else:
                    sneks += 1
            except:
                pass
    return sneks


def find_corner(tiles):
    edge_count = dict()
    for tile in tiles:
        for e in tile["edges"]:
            edge_count[e] = edge_count.setdefault(e, 0) + 1

    for tile in tiles:
        n2 = edge_count[tile["edges"][0]] + edge_count[tile["edges"][3]]
        if n2 == 8:
            return tile


def solve(tiles):
    square_size = int(math.sqrt(len(tiles) // 8))

    solution = [[None for x in range(square_size)] for y in range(square_size)]
    used = set()

    for y in range(square_size):
        for x in range(square_size):
            if x == 0 and y == 0:
                solution[y][x] = find_corner(tiles)
                used |= {solution[y][x]["id"]}
                continue

            for tile in tiles:
                up = (
                    True
                    if y == 0
                    else tile["edges"][0] == solution[y - 1][x]["edges"][2]
                )
                left = (
                    True
                    if x == 0
                    else tile["edges"][3] == solution[y][x - 1]["edges"][1]
                )

                if up and left and tile["id"] not in used:
                    solution[y][x] = tile
                    used |= {solution[y][x]["id"]}
                    break
    return solution


def parse(f):
    def parse_tile(t):
        [id, data] = t.split("\n", 1)

        id = int(id.split(" ")[1][:-1])

        data = data.split("\n")

        for d in possible(data):

            edges = [
                int("".join(["1" if pixel == "#" else "0" for pixel in d[0]]), 2),
                int("".join(["1" if line[-1] == "#" else "0" for line in d]), 2),
                int("".join(["1" if pixel == "#" else "0" for pixel in d[-1]]), 2),
                int("".join(["1" if line[0] == "#" else "0" for line in d]), 2),
            ]

            yield {"id": id, "data": d, "edges": edges}

    tiles = f.read().strip().split("\n\n")
    for tile in tiles:
        yield from parse_tile(tile)


with open("day20.txt", "r", encoding="utf-8") as f:
    tiles = list(parse(f))

    solution = solve(tiles)

    p1 = (
        solution[0][0]["id"]
        * solution[0][-1]["id"]
        * solution[-1][0]["id"]
        * solution[-1][-1]["id"]
    )

    print(f"Part 1: {p1}")

    image = []
    for y1 in range(len(solution)):

        for y2 in range(1, 9):
            line = ""
            for x1 in range(len(solution[0])):
                line += solution[y1][x1]["data"][y2][1:-1]
            image.append(line)

    p2 = None
    for d in possible(image):
        sneks = count_snek(d)
        if sneks > 0:
            p2 = count(image) - count(SNEK) * sneks
            break

    print(f"Part 2: {p2}")
