rows, cols = [int(c) for c in input().split()]
user_input = input()

matrix = [["" for _ in range(cols)] for row in range(rows)]

index = 0

for row in range(rows):
    if row % 2 == 0:
        for col in range(cols):
            matrix[row][col] = user_input[index]
            index = (index + 1) % len(user_input)
    else:
        for col in range(cols - 1, -1, -1):
            matrix[row][col] = user_input[index]
            index = (index + 1) % len(user_input)

for row in matrix:
    print(f"".join(row))
