expression = input()

stack = []

for index in range(len(expression)):
    if expression[index] == "(":
        stack.append(index)
    elif expression[index] == ")":
        most_recent = stack.pop()
        print(expression[most_recent : index + 1])


# Inputs:
# 1 + (2 - (2 + 3) * 4 / (3 + 1)) * 5
# (2 + 3) - (2 + 3)
