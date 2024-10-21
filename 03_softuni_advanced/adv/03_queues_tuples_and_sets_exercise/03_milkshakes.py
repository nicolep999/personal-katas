from collections import deque

user_input_chocolate = [int(x) for x in input().split(", ")]
user_input_milk = deque(int(x) for x in input().split(", "))

total = 0

while user_input_chocolate and user_input_milk and total < 5:

    if user_input_chocolate[-1] <= 0 and user_input_milk[0] <= 0:
        user_input_chocolate.pop()
        user_input_milk.popleft()
        continue
    if user_input_chocolate[-1] <= 0:
        user_input_chocolate.pop()
        continue
    if user_input_milk[0] <= 0:
        user_input_milk.popleft()
        continue

    if user_input_chocolate[-1] == user_input_milk[0]:
        total += 1
        user_input_chocolate.pop()
        user_input_milk.popleft()
    else:
        user_input_milk.rotate(-1)
        user_input_chocolate[-1] -= 5


if total == 5:
    print("Great! You made all the chocolate milkshakes needed!")
else:
    print("Not enough milkshakes.")

print(
    f"Chocolate: {', '.join([str(n) for n in user_input_chocolate])}"
    if user_input_chocolate
    else "Chocolate: empty"
)
print(
    f"Milk: {', '.join([str(n) for n in user_input_milk])}"
    if user_input_milk
    else "Milk: empty"
)
