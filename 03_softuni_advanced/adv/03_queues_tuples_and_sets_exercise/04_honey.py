from collections import deque

bees = deque([int(x) for x in input().split()])
nectar = [int(x) for x in input().split()]
operators = deque(input().split())
honey = 0


def calculate(b, n, o):
    if o == "+":
        return abs(b + n)
    elif o == "-":
        return abs(b - n)
    elif o == "*":
        return abs(b * n)
    elif o == "/":
        if n == 0:
            return 0
        else:
            return abs(b / n)


while bees and nectar:
    if nectar[-1] >= bees[0]:
        operator = operators.popleft()
        bee = bees.popleft()
        nec = nectar.pop()
        honey += calculate(bee, nec, operator)
    else:
        nectar.pop()

print(f"Total honey made: {honey}")
if bees:
    print(f"Bees left: {', '.join([str(b) for b in bees])}")
if nectar:
    print(f"Nectar left: {', '.join([str(b) for b in nectar])}")
