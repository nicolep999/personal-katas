rows, columns = map(int, input().split())

matrix = [[int(x) for x in input().split()] for _ in range(rows)]

final_list = []

total_sum = float("-inf")

for i in range(rows - 2):
    final_list.append([])
    for j in range(columns - 2):
        temp_sum = (
            sum(matrix[i][j : j + 3])
            + sum(matrix[i + 1][j : j + 3])
            + sum(matrix[i + 2][j : j + 3])
        )
        if temp_sum > total_sum:
            total_sum = temp_sum
            final_list = [
                matrix[i][j : j + 3],
                matrix[i + 1][j : j + 3],
                matrix[i + 2][j : j + 3],
            ]


print(f"Sum = {total_sum}")
for i in range(len(final_list)):
    print(f"{' '.join(map(str, final_list[i]))}")
