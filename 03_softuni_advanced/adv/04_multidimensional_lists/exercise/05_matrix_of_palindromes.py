rows, columns = map(int, input().split())

matrix = []

for i in range(rows):
    row = []
    for j in range(columns):
        first_last_letter = chr(97 + i)
        middle_letter = chr(97 + i + j)
        palindrome = first_last_letter + middle_letter + first_last_letter
        row.append(palindrome)
    matrix.append(row)

for row in matrix:
    print(" ".join(row))
