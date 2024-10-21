from collections import deque

user_input = deque(input().split())

colors = ["red", "blue", "yellow", "orange", "purple", "green"]

result = []


def check_color(c, arr):
    if c == "orange" and "red" in arr and "yellow" in arr:
        return True
    elif c == "purple" and "blue" in arr and "red" in arr:
        return True
    elif c == "green" and "blue" in arr and "yellow" in arr:
        return True
    elif c == "red" or c == "blue" or c == "yellow":
        return True
    else:
        return False


while user_input:

    first_char = user_input.popleft()
    last_char = user_input.pop() if user_input else ""
    for color in (first_char + last_char, last_char + first_char):
        if color in colors:
            result.append(color)
            break
    else:
        if len(first_char) > 1:
            user_input.insert(len(user_input) // 2, first_char[:-1])
        if len(last_char) > 1:
            user_input.insert(
                len(user_input) // 2, last_char[:-1]
            )  # Ако брейкнем, не стига до тук, else ще се изпълни само ако for е изпълнен

for c in result:
    if not check_color(c, result):
        result.remove(c)
print(result)
