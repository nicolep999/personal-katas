class MatrixContentError(Exception):
    pass


class MatrixSizeError(Exception):
    pass


def rotate_matrix(input_matrix):
    matrix_length = len(input_matrix)

    for i in range(matrix_length):
        for j in range(i, matrix_length):
            input_matrix[i][j], input_matrix[j][i] = (
                input_matrix[j][i],
                input_matrix[i][j],
            )

    for i in range(matrix_length):
        input_matrix[i].reverse()


matrix = []

while True:
    row_input = input()
    if not row_input:
        break
    row = list(map(str.strip, row_input.split()))
    matrix.append(row)

try:
    if not all(len(row) == len(matrix) for row in matrix):
        raise MatrixSizeError("The size of the matrix is not a perfect square")

    for row in matrix:
        for value in row:
            if not value.isdigit() and not (value[1:].isdigit() and value[0] == "-"):
                raise MatrixContentError("The matrix must consist of only integers")

    matrix = [[int(value) for value in row] for row in matrix]

    rotate_matrix(matrix)

    for row in matrix:
        print(*row, sep=" ")

except (MatrixContentError, MatrixSizeError) as error:
    print(error)
