# Trying alternative solution - NOT THE BEST!


def solution(number) -> int:

    if number <= 0:
        return 0

    x = 0
    y = 0

    solution_set = {x, y}

    for n in range(number):

        x = x + 3
        y = y + 5

        if x < number:
            solution_set.add(x)
        if y < number:
            solution_set.add(y)

    return sum(solution_set)
