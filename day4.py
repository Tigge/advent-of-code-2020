import functools
import operator
import pprint
import re


def parse(f):
    blocks = f.read().split("\n\n")
    blocks = map(lambda b: map(lambda i: tuple(i.split(":")), b.split()), blocks)
    return map(dict, blocks)


def valid1(p):
    return {"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"} - p.keys() == set()


def valid2(p):
    try:

        height, heightunit = re.fullmatch(r"([0-9]{2,3})(cm|in)", p["hgt"]).groups()
        return (
            1920 <= int(p["byr"]) <= 2002
            and 2010 <= int(p["iyr"]) <= 2020
            and 2020 <= int(p["eyr"]) <= 2030
            and (
                (heightunit == "cm" and 150 <= int(height) <= 193)
                or (heightunit == "in" and 59 <= int(height) <= 76)
            )
            and bool(re.fullmatch(r"#[0-9a-f]{6}", p["hcl"]))
            and p["ecl"] in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
            and bool(re.fullmatch(r"[0-9]{9}", p["pid"]))
        )
    except:
        return False


with open("day4.txt", "r", encoding="utf-8") as f:
    passports = list(parse(f))
    print(f"Part 1: {sum(map(valid1, passports))}")
    print(f"Part 2: {sum(map(valid2, passports))}")
