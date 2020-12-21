import functools
import operator


def parse(f):
    lines = f.read().strip().split("\n")

    for line in lines:
        [ingredients, allergens] = line[:-1].split(" (contains ")
        yield set(ingredients.split(" ")), set(allergens.split(", "))


with open("day21.txt", "r", encoding="utf-8") as f:
    stuff = list(parse(f))

    all_allergens = functools.reduce(
        operator.or_, [safe_ingredient[1] for safe_ingredient in stuff]
    )
    all_ingredients = functools.reduce(
        operator.or_, [safe_ingredient[0] for safe_ingredient in stuff]
    )

    possible = dict()
    for allergen in all_allergens:
        possible[allergen] = set(all_ingredients)
        for ingredients, allergens in stuff:
            if allergen in allergens:
                possible[allergen] &= ingredients

    allergen_ingredients = functools.reduce(operator.or_, possible.values())

    safe_ingrediens = all_ingredients - allergen_ingredients

    p1 = 0
    for ingredients, _ in stuff:
        for safe_ingredient in safe_ingrediens:
            if safe_ingredient in ingredients:
                p1 += 1

    p1 = len(all_ingredients) - len(allergen_ingredients)

    print(f"Part 1: {p1}")

    p2 = ",".join(sorted(list(allergen_ingredients)))

    for i in range(len(possible)):
        for allergen, ingredients in possible.items():
            if len(ingredients) == 1:
                for allergen2, ingredients2 in possible.items():
                    if allergen != allergen2:
                        possible[allergen2] -= ingredients

    p2 = ",".join([list(possible[k])[0] for k in sorted(possible.keys())])

    print(f"Part 2: {p2}")
