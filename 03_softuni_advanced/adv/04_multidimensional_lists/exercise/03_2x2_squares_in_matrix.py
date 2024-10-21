rows, columns = map(int, input().split())

matrix = [[x for x in input().split()] for _ in range(rows)]

square_matrix = 0

for i in range(rows - 1):
    for j in range(columns - 1):
        if (
            matrix[i][j] == matrix[i][j + 1]
            and matrix[i + 1][j] == matrix[i + 1][j + 1]
            and matrix[i][j] == matrix[i + 1][j]
        ):
            square_matrix += 1

print(square_matrix)
