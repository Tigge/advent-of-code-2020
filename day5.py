def parse(f):
    def parse_seat(s):
        row = int("".join(map(lambda x: "1" if x == "B" else "0", s[:7])), 2)
        col = int("".join(map(lambda x: "1" if x == "R" else "0", s[7:])), 2)
        return row * 8 + col

    return sorted(map(parse_seat, f.read().strip().split("\n")))


with open("day5.txt", "r", encoding="utf-8") as f:
    seats = list(parse(f))

    print(f"Part 1: {max(seats)}")
    print(
        f"Part 2: {next(s for s in zip(seats[:-1], seats[1:]) if s[0] != s[1] - 1)[0] + 1}"
    )
