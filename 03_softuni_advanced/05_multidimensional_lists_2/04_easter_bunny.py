n = int(input())

matrix = []

starting_position = []

for row in range(n):
    matrix.append([x for x in input().split()])
    for column in range(n):
        if matrix[row][column] == "B":
            starting_position = [row, column]

bunny_path = []
bunny_direction = ""

possible_moves = {"up": (-1, 0), "down": (1, 0), "left": (0, -1), "right": (0, 1)}

max_sum = float("-inf")

for direction, move in possible_moves.items():

    current_sum = 0
    temp_path = []

    row = starting_position[0] + move[0]
    col = starting_position[1] + move[1]

    while 0 <= row < n and 0 <= col < n:
        if matrix[row][col] == "X":
            break
        current_sum += int(matrix[row][col])
        temp_path.append([row, col])
        row += move[0]
        col += move[1]

    if current_sum > max_sum and temp_path:
        max_sum = current_sum
        bunny_path = temp_path
        bunny_direction = direction

print(bunny_direction)
[print(row) for row in bunny_path]
print(max_sum)
