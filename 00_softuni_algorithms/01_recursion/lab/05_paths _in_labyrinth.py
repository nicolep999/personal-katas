rows = int(input())
cols = int(input())

lab = [list(input()) for _ in range(rows)]


def out_of_bounds(row: int, col: int, lab: list) -> bool:
    if row < 0 or col < 0 or row >= len(lab) or col >= len(lab[0]):
        return True
    return False


def hit_wall(row: int, col: int, lab: list) -> bool:
    if lab[row][col] == "*":
        return True
    return False


def node_visited(row: int, col: int, lab: list) -> bool:
    if lab[row][col] == "v":
        return True
    return False


def find_all_paths(row: int, col: int, lab: list, direction: str, path: list):

    if (
        out_of_bounds(row, col, lab)
        or hit_wall(row, col, lab)
        or node_visited(row, col, lab)
    ):
        return

    path.append(direction)

    if lab[row][col] == "e":
        print("".join(path))
    else:
        lab[row][col] = "v"
        find_all_paths(row - 1, col, lab, "U", path)
        find_all_paths(row + 1, col, lab, "D", path)
        find_all_paths(row, col - 1, lab, "L", path)
        find_all_paths(row, col + 1, lab, "R", path)
        lab[row][col] = "-"

    path.pop()


find_all_paths(0, 0, lab, "", [])
