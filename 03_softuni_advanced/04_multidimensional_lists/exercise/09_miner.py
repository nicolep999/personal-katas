n = int(input())

commands = [c for c in input().split()]

matrix = [[j for j in input().split()] for _ in range(n)]


def valid_move(x, y, command):
    if command == "up":
        if x > 0:
            x -= 1
            return [x, y]
    elif command == "down":
        if x < len(matrix) - 1:
            x += 1
            return [x, y]
    elif command == "left":
        if y > 0:
            y -= 1
            return [x, y]
    elif command == "right":
        if y < len(matrix) - 1:
            y += 1
            return [x, y]
    return False


def get_starting_position(m):
    for row in range(len(m)):
        for col in range(len(m[row])):
            if matrix[row][col] == "s":
                return row, col


position_row, position_col = get_starting_position(matrix)

current_position = [position_row, position_col]


def coal_finder():
    coal = 0
    for row in range(n):
        for col in range(n):
            if matrix[row][col] == "c":
                coal += 1
    return coal


def main():
    user_coal = coal_finder()
    for command in commands:
        temp_position = valid_move(current_position[0], current_position[1], command)
        if temp_position:
            matrix[current_position[0]][current_position[1]] = "*"
            current_position[0], current_position[1] = (
                temp_position[0],
                temp_position[1],
            )
            if matrix[current_position[0]][current_position[1]] == "e":
                print(f"Game over! ({current_position[0]}, {current_position[1]})")
                return
            elif matrix[current_position[0]][current_position[1]] == "c":
                user_coal -= 1
        else:
            continue
    if user_coal == 0:
        print(f"You collected all coal! {(current_position[0], current_position[1])}")
    elif user_coal > 0:
        print(
            f"{user_coal} pieces of coal left. {(current_position[0], current_position[1])}"
        )


main()
