n = int(input())

m = []
knights = []

for row in range(n):
    m.append([x for x in input()])
    for col in range(n):
        if m[row][col] == "K":
            knights.append([row, col])

removed = 0
possible_moves = (
    (1, 2),
    (2, 1),
    (-1, 2),
    (2, -1),
    (-2, 1),
    (1, -2),
    (-1, -2),
    (-2, -1),
)

while True:
    max_hits = 0
    max_knight = [0, 0]

    for i, j in knights:
        hits = 0

        for move in possible_moves:
            next_row = i + move[0]
            next_col = j + move[1]
            if 0 <= next_row < n and 0 <= next_col < n:
                if m[next_row][next_col] == "K":
                    hits += 1

        if hits > max_hits:
            max_hits = hits
            max_knight = [i, j]

    if max_hits == 0:
        print(removed)
        break

    knights.remove(max_knight)
    m[max_knight[0]][max_knight[1]] = "0"
    removed += 1
