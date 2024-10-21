n = int(input())

matrix = [[int(j) for j in input().split()] for _ in range(n)]


primary = 0
secondary = 0

# for i in range(n):
#     primary.append(matrix[i][i])
#
# for i in range(0, n):
#     j = len(matrix) - i - 1
#     secondary.append(matrix[i][j])
for i, j in zip(range(0, len(matrix)), range(len(matrix) - 1, -1, -1)):
    a = matrix[i][i]
    b = matrix[i][j]
    primary += a
    secondary += b

difference = abs(primary - secondary)

print(difference)
