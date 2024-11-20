from itertools import permutations


def possible_permutations(col: list):
    for perm in permutations(col):
        yield list(perm)


[print(n) for n in possible_permutations([1, 2, 3])]
