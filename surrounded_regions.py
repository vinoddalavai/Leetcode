from collections import defaultdict
from typing import List


class SurroundedRegions:
    def solve(self, board: List[List[str]]):
        rows, columns = len(board), len(board[0])

        def capture(row, col):
            if (row not in range(rows) or
                    col not in range(columns) or
                    board[row][col] != 'O'):
                return

            board[row][col] = 'T'
            directions = [
                [1, 0],
                [-1, 0],
                [0, 1],
                [0, -1]
            ]
            for dr, dc in directions:
                capture(row + dr, col + dc)

        for r in range(rows):
            for c in range(columns):
                if board[r][c] == 'O' and (r in [0, rows - 1] or (c in [0, columns - 1])):
                    capture(r, c)

        for r in range(rows):
            for c in range(columns):
                if board[r][c] == 'O':
                    board[r][c] = 'X'

        for r in range(rows):
            for c in range(columns):
                if board[r][c] == 'T':
                    board[r][c] = 'O'


input_board = [["X", "X", "X", "X"], ["X", "O", "O", "X"], ["X", "X", "O", "X"], ["X", "O", "X", "X"]]
obj = SurroundedRegions()
obj.solve(input_board)
print("Marking surrounding regions:")
print(input_board)
