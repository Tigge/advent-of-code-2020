DEG = {"N": 90, "S": 270, "W": 180, "E": 0}


def parse(f):
    return list(map(lambda l: (l[0], int(l[1:])), f.read().strip().split("\n")))


def move(pos, turn, value):
    if turn % 360 == 0:
        return (pos[0] + value, pos[1])
    elif turn % 360 == 90:
        return (pos[0], pos[1] - value)
    elif turn % 360 == 180:
        return (pos[0] - value, pos[1])
    elif turn % 360 == 270:
        return (pos[0], pos[1] + value)


def p1(turns):
    pos = (0, 0)
    turn = 0

    for action, value in turns:
        if action in ["N", "S", "E", "W"]:
            pos = move(pos, DEG[action], value)
        elif action == "L":
            turn += value
        elif action == "R":
            turn -= value
        elif action == "F":
            pos = move(pos, turn, value)

    return abs(pos[0]) + abs(pos[1])


def turn(pos, v):
    if v % 360 == 0:
        return pos
    elif v % 360 == 90:
        return (pos[1], -pos[0])
    elif v % 360 == 180:
        return (-pos[0], -pos[1])
    elif v % 360 == 270:
        return (-pos[1], pos[0])


def p2(turns):
    way = (10, -1)
    pos = (0, 0)

    for action, value in turns:
        if action in ["N", "S", "E", "W"]:
            way = move(way, DEG[action], value)
        elif action == "L":
            way = turn(way, value)
        elif action == "R":
            way = turn(way, -value)
        elif action == "F":
            pos = (pos[0] + way[0] * value, pos[1] + way[1] * value)

    return abs(pos[0]) + abs(pos[1])


with open("day12.txt", "r", encoding="utf-8") as f:
    turns = parse(f)

    print(f"Part 1: {p1(turns)}")
    print(f"Part 2: {p2(turns)}")
