n = int(input())

matrix = [[int(x) for x in input().split()] for _ in range(n)]


bombs = [x for x in input().split()]


def get_cells(x, y, size) -> list:
    cells = []

    if x - 1 in range(size) and y - 1 in range(size):
        cells.append((x - 1, y - 1))
    if x in range(size) and y - 1 in range(size):
        cells.append((x, y - 1))
    if x + 1 in range(size) and y - 1 in range(size):
        cells.append((x + 1, y - 1))
    if x - 1 in range(size) and y in range(size):
        cells.append((x - 1, y))
    if x + 1 in range(size) and y in range(size):
        cells.append((x + 1, y))
    if x - 1 in range(size) and y + 1 in range(size):
        cells.append((x - 1, y + 1))
    if x in range(size) and y + 1 in range(size):
        cells.append((x, y + 1))
    if x + 1 in range(size) and y + 1 in range(size):
        cells.append((x + 1, y + 1))

    return cells


for bomb in bombs:
    i, j = map(int, bomb.split(","))
    bomb_power = matrix[i][j]
    if bomb_power > 0:
        to_kill = get_cells(i, j, n)
        for r, c in to_kill:
            if matrix[r][c] > 0:
                matrix[r][c] -= bomb_power
        matrix[i][j] = 0

alive_cells = 0
result_sum = 0

for row in range(n):
    for col in range(n):
        if matrix[row][col] > 0:
            alive_cells += 1
            result_sum += matrix[row][col]

print(f"Alive cells: {alive_cells}")
print(f"Sum: {result_sum}")
for row in matrix:
    print(" ".join(map(str, row)))
