presents = int(input())
n = int(input())

matrix = []
current_position = []

total_kids = 0
total_kids_gifted = 0

for i in range(n):
    matrix.append([x for x in input().split()])
    for j in range(n):
        if matrix[i][j] == "S":
            current_position = [i, j]
        elif matrix[i][j] == "V":
            total_kids += 1


possible_moves = {"up": (-1, 0), "down": (1, 0), "left": (0, -1), "right": (0, 1)}

while presents > 0:
    command = input()

    if command == "Christmas morning":
        break

    row, col = (
        current_position[0] + possible_moves[command][0],
        current_position[1] + possible_moves[command][1],
    )

    if 0 <= row < n and 0 <= col < n:
        if matrix[row][col] == "V":
            presents -= 1
            total_kids_gifted += 1
            matrix[row][col] = "-"
        elif matrix[row][col] == "C":
            for direction in possible_moves.values():
                next_row, next_col = row + direction[0], col + direction[1]
                if matrix[next_row][next_col] in "VX" and presents > 0:
                    presents -= 1
                    if matrix[next_row][next_col] == "V":
                        total_kids_gifted += 1
                    matrix[next_row][next_col] = "-"

        matrix[current_position[0]][current_position[1]] = "-"
        current_position = [row, col]
        matrix[row][col] = "S"

if presents < 1 and total_kids - total_kids_gifted > 0:
    print(f"Santa ran out of presents!")

[print(*row) for row in matrix]
if total_kids - total_kids_gifted > 0:
    print(f"No presents for {total_kids - total_kids_gifted} nice kid/s.")
else:
    print(f"Good job, Santa! {total_kids_gifted} happy nice kid/s.")
