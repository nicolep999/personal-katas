n = int(input())

matrix = []

starting_position = []

for row in range(n):

    matrix.append([x for x in input().split()])

    for col in range(n):
        if matrix[row][col] == "A":
            matrix[row][col] = "*"
            starting_position = [row, col]

possible_moves = {"up": (-1, 0), "down": (1, 0), "left": (0, -1), "right": (0, 1)}
total_sum = 0

while total_sum < 10:

    command = input()
    move = possible_moves[command]

    row = starting_position[0] + move[0]
    col = starting_position[1] + move[1]

    if row < 0 or row >= n or col < 0 or col >= n:
        break
    if matrix[row][col] == "R":
        matrix[row][col] = "*"
        break

    if matrix[row][col] not in "*.":
        total_sum += int(matrix[row][col])

    matrix[row][col] = "*"
    starting_position = [row, col]

if total_sum >= 10:
    print("She did it! She went to the party.")
else:
    print("Alice didn't make it to the tea party.")

[print(*row) for row in matrix]
