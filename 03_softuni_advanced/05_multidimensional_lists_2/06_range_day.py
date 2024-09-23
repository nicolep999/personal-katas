n = 5

matrix = []
targets = 0

current_position = []

for row in range(n):
    matrix.append([x for x in input().split()])
    for column in range(n):
        if matrix[row][column] == "x":
            targets += 1
        elif matrix[row][column] == "A":
            current_position = [row, column]

possible_moves = {"up": (-1, 0), "down": (1, 0), "left": (0, -1), "right": (0, 1)}

targets_down = []

for _ in range(int(input())):

    command = input().split()

    if command[0] == "shoot":

        row = current_position[0] + possible_moves[command[1]][0]
        col = current_position[1] + possible_moves[command[1]][1]

        while 0 <= row < n and 0 <= col < n:
            if matrix[row][col] == "x":
                matrix[row][col] = "."
                targets_down.append([row, col])
                targets -= 1
                break
            row += possible_moves[command[1]][0]
            col += possible_moves[command[1]][1]

        if targets <= 0:
            print(f"Training completed! All {len(targets_down)} targets hit.")
            break

    elif command[0] == "move":
        row = current_position[0] + possible_moves[command[1]][0] * int(command[2])
        col = current_position[1] + possible_moves[command[1]][1] * int(command[2])
        if 0 <= row < n and 0 <= col < n and matrix[row][col] == ".":
            matrix[row][col] = "A"
            current_position = [row, col]

if targets > 0:
    print(f"Training not completed! {targets} targets left.")

[print(row) for row in targets_down]
