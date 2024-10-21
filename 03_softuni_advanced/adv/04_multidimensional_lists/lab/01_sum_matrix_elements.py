row_count, col_count = [int(el) for el in input().split(", ")]

matrix = []

elements_sum = 0

for i in range(row_count):
    row_data = [int(el) for el in input().split(", ")]
    matrix.append(row_data)
    elements_sum += sum(row_data)

print(elements_sum)
print(matrix)

"""
3, 6
7, 1, 3, 3, 2, 1
1, 3, 9, 8, 5, 6
4, 6, 7, 9, 1, 0
"""
