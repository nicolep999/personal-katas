n = int(input())

matrix = [[int(x) for x in input().split()] for _ in range(n)]

while True:
    user_input = input().split()
    command = user_input[0]
    if command == "END":
        for row in matrix:
            print(*row)
        break

    row, column, value = map(int, user_input[1:])

    if (
        row < 0
        or column < 0
        or row > (len(matrix) - 1)
        or column > (len(matrix[0]) - 1)
    ):
        print("Invalid coordinates")
        continue
    elif command == "Add":
        matrix[row][column] += value
    elif command == "Subtract":
        matrix[row][column] -= value
