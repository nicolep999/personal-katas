stack = []
iterations = int(input())

for _ in range(iterations):
    user_command = list(map(int, input().split()))
    command = user_command[0]
    if len(user_command) == 2:
        user_input = user_command[1]
        stack.append(user_input)
    else:
        if stack:
            if command == 2:
                stack.pop()
            elif command == 3:
                print(max(stack))
            elif command == 4:
                print(min(stack))


print(", ".join(map(str, reversed(stack))))
