import functools
import operator
import copy


def parse(f):
    players = f.read().strip().split("\n\n")
    return [list(map(int, player.split("\n")[1:])) for player in players]


def score(players):
    cards = players[0] + players[1]
    return functools.reduce(
        operator.add, [m * c for m, c in zip(range(len(cards), 0, -1), cards)]
    )


def hand_hash(players):
    return ",".join(map(str, players[0])) + ":" + ",".join(map(str, players[1]))


def part1(players):
    player1, player2 = copy.deepcopy(players)

    while len(player1) != 0 and len(player2) != 0:
        if player1[0] > player2[0]:
            player1.append(player1.pop(0))
            player1.append(player2.pop(0))
        else:
            player2.append(player2.pop(0))
            player2.append(player1.pop(0))

    return player1, player2


def part2(players):
    def recurse(players):
        history = set()
        player1, player2 = copy.deepcopy(players)

        while len(player1) != 0 and len(player2) != 0:
            p1win = True

            if hand_hash((player1, player2)) in history:
                player1.append(player1.pop(0))
                player1.append(player2.pop(0))
                return ([1], [])

            history.add(hand_hash((player1, player2)))

            p1card = player1.pop(0)
            p2card = player2.pop(0)

            if len(player1) >= p1card and len(player2) >= p2card:
                p1sub, p2sub = recurse((player1[:p1card], player2[:p2card]))
                p1win = len(p1sub) > len(p2sub)
            else:
                p1win = p1card > p2card

            if p1win:
                player1.append(p1card)
                player1.append(p2card)
            else:
                player2.append(p2card)
                player2.append(p1card)

        return [player1, player2]

    return recurse(players)


with open("day22.txt", "r", encoding="utf-8") as f:
    players = list(parse(f))

    p1 = score(part1(players))
    print(f"Part 1: {p1}")

    p2 = score(part2(players))
    print(f"Part 2: {p2}")
