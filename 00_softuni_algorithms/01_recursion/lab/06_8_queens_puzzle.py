## LeetCode Solution

from typing import List


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:

        def is_valid(board, row, col):
            for i in range(row):
                if (
                    board[i] == col
                    or board[i] - i == col - row
                    or board[i] + i == col + row
                ):
                    return False
            return True

        def place_queens(n, row, board):
            if row == n:
                result.append(board[:])
                return
            for col in range(n):
                if is_valid(board, row, col):
                    board[row] = col
                    place_queens(n, row + 1, board)

        result = []
        place_queens(n, 0, [-1] * n)
        return [["." * i + "Q" + "." * (n - i - 1) for i in sol] for sol in result]


## Judge Solution

# n = 8
# board = [["-"] * n for _ in range(n)]


# def can_place_queen(row, col, rows, cols, left_diagonals, right_diagonals):
#     if (
#         row in rows
#         or col in cols
#         or row - col in left_diagonals
#         or row + col in right_diagonals
#     ):
#         return False
#     return True


# def set_queen(row, col, board, rows, cols, left_diagonals, right_diagonals):
#     board[row][col] = "*"
#     rows.add(row)
#     cols.add(col)
#     left_diagonals.add(row - col)
#     right_diagonals.add(row + col)


# def unset_queen(row, col, board, rows, cols, left_diagonals, right_diagonals):
#     board[row][col] = "-"
#     rows.remove(row)
#     cols.remove(col)
#     left_diagonals.remove(row - col)
#     right_diagonals.remove(row + col)


# def print_board(board):
#     for row in board:
#         print(" ".join(row))
#     print()


# def put_queens(row, board, rows, cols, left_diagonals, right_diagonals):
#     if row == n:
#         print_board(board)
#         return
#     for col in range(n):
#         if can_place_queen(row, col, rows, cols, left_diagonals, right_diagonals):
#             set_queen(row, col, board, rows, cols, left_diagonals, right_diagonals)
#             put_queens(row + 1, board, rows, cols, left_diagonals, right_diagonals)
#             unset_queen(row, col, board, rows, cols, left_diagonals, right_diagonals)


# put_queens(0, board, set(), set(), set(), set())
