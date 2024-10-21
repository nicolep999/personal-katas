def find_starting_position(matrix, n):
    for row in range(n):
        for col in range(n):
            if matrix[row][col] == "P":
                return row, col


def main():
    n = int(input())
    matrix = [[x for x in input().split()] for _ in range(n)]

    stars_collected = 2

    temp_position = find_starting_position(matrix, n)
    current_position = temp_position
    matrix[current_position[0]][current_position[1]] = "."

    while True:

        command = input()

        if command == "right":
            temp_position = (
                temp_position[0],
                temp_position[1] + 1,
            )

        elif command == "left":
            temp_position = (
                temp_position[0],
                temp_position[1] - 1,
            )

        elif command == "up":
            temp_position = (
                temp_position[0] - 1,
                temp_position[1],
            )

        elif command == "down":
            temp_position = (
                temp_position[0] + 1,
                temp_position[1],
            )

        if (
            temp_position[0] < 0
            or temp_position[0] >= n
            or temp_position[1] < 0
            or temp_position[1] >= n
        ):
            current_position = (0, 0)
            temp_position = current_position

        if matrix[temp_position[0]][temp_position[1]] == "#":
            temp_position = current_position
            stars_collected -= 1

        elif matrix[temp_position[0]][temp_position[1]] == "*":
            stars_collected += 1
            matrix[temp_position[0]][temp_position[1]] = "."

        current_position = temp_position

        if stars_collected <= 0:
            print("Game over! You are out of any stars.")
            matrix[current_position[0]][current_position[1]] = "P"
            break

        elif stars_collected >= 10:
            print(f"You won! You have collected {stars_collected} stars.")
            matrix[current_position[0]][current_position[1]] = "P"
            break

    print(f"Your final position is [{current_position[0]}, {current_position[1]}]")

    for row in matrix:
        print(" ".join(row), sep="\n")


if __name__ == "__main__":
    main()
