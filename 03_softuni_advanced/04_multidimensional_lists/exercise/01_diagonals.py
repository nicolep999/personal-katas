n = int(input())

matrix = [[int(j) for j in input().split(",")] for _ in range(n)]


primary = []
secondary = []

# for i in range(n):
#     primary.append(matrix[i][i])
#
# for i in range(0, n):
#     j = len(matrix) - i - 1
#     secondary.append(matrix[i][j])

for i, j in zip(range(0, len(matrix)), range(len(matrix) - 1, -1, -1)):
    a = matrix[i][i]
    b = matrix[i][j]
    primary.append(a)
    secondary.append(b)


print(f"Primary diagonal: {', '.join(str(x) for x in primary)}. Sum: {sum(primary)}")
print(
    f"Secondary diagonal: {', '.join(str(x) for x in secondary)}. Sum: {sum(secondary)}"
)
