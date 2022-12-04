"""
Approach: Arrays and Hashing
Time Complexity: O(N^2)
Space Complexity: O(N^2)
"""

from collections import defaultdict
from typing import List


class ValidSudoku:
    def _is_valid_sudoku(self, board: List[List[str]]) -> bool:
        # initialize rows, cols and boxes to be dictionaries with values as set
        rows, cols, boxes = defaultdict(set), defaultdict(set), defaultdict(set)
        # iterate through every row of the board
        for row in range(9):
            # iterate through every column of the board
            for col in range(9):
                # get the value of that cell on the board
                value = board[row][col]
                # skip if value is not a number
                if value == '.':
                    continue
                # check if value exists in rows, cols or boxes
                if (value in rows[row] or
                        value in cols[col] or
                        value in boxes[(row//3, col//3)]):
                    # if present, return False
                    return False
                # if value does not exist then add to rows, cols and boxes
                rows[row].add(value)
                cols[col].add(value)
                boxes[(row//3, col//3)].add(value)
        # if control reaches here then every row, column and box has non-repetitive digits
        return True

    def process(self, input_board: List[List[str]]) -> None:
        print(f"\nOutput >> {self._is_valid_sudoku(input_board)}\n")


if __name__ == '__main__':
    size = 9
    input_sudoku_board = [["." for _ in range(size)] for _ in range(size)]
    for r in range(size):
        for c in range(size):
            v = input(f"Enter number at position ({r}, {c}): ")
            if not v:
                continue
            else:
                input_sudoku_board[r][c] = v
    print("\nYour board is as follows:")
    for r in range(size):
        for c in range(size):
            print(input_sudoku_board[r][c], end="\t")
        print()
    ValidSudoku().process(input_sudoku_board)
