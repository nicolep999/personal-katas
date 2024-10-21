rows, cols = [int(num) for num in input().split()]

matrix = [[n for n in input().split()] for _ in range(rows)]

commands = ["swap", "END"]

while True:
    user_input = input().split()
    cmd = user_input[0]

    if cmd == "END":
        break
    elif len(user_input) != 5 or cmd not in commands:
        print("Invalid input!")
        continue
    elif cmd == "swap":
        row_1 = int(user_input[1])
        col_1 = int(user_input[2])
        row_2 = int(user_input[3])
        col_2 = int(user_input[4])
        if (
            0 <= row_1 < rows
            and 0 <= row_2 < rows
            and 0 <= col_1 < cols
            and 0 <= col_2 < cols
        ):
            matrix[row_1][col_1], matrix[row_2][col_2] = (
                matrix[row_2][col_2],
                matrix[row_1][col_1],
            )
            for row in matrix:
                print(" ".join(map(str, row)))
        else:
            print("Invalid input!")
            continue
