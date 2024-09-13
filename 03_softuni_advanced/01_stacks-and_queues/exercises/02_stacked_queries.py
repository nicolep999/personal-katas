# stack = []
# iterations = int(input())
#
# for _ in range(iterations):
#     user_command = list(map(int, input().split()))
#     command = user_command[0]
#     if len(user_command) == 2:
#         user_input = user_command[1]
#         stack.append(user_input)
#     else:
#         if stack:
#             if command == 2:
#                 stack.pop()
#             elif command == 3:
#                 print(max(stack))
#             elif command == 4:
#                 print(min(stack))
#
#
# print(", ".join(map(str, reversed(stack))))

# Teacher solution

number_of_queries = int(input())
my_stack = []

functions = {
    "1": lambda number: my_stack.append(int(number)),
    "2": lambda: my_stack.pop() if my_stack else None,
    "3": lambda: print(max(my_stack)) if my_stack else None,
    "4": lambda: print(min(my_stack)) if my_stack else None,
}

for _ in range(number_of_queries):
    command = input().split()
    functions[command[0]](*command[1:])

print(*reversed(my_stack), sep=", ")
