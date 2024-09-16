from collections import deque

user_input = input().split()
queue = deque()


def calculate(a: int, b: int, operator: str) -> int:
    if operator == "+":
        return a + b
    elif operator == "-":
        return a - b
    elif operator == "*":
        return a * b
    elif operator == "/":
        return a // b


for x in user_input:
    if x not in "+-*/":
        queue.append(int(x))
    else:
        while len(queue) > 1:
            num1 = queue.popleft()
            num2 = queue.popleft()
            queue.appendleft(calculate(num1, num2, x))

print(queue.popleft())
