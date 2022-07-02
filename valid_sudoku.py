from collections import defaultdict
from typing import List


class ValidSudoku:
    def is_valid_sudoku_using_hashset(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        columns = defaultdict(set)
        boxes = defaultdict(set)
        for row in range(9):
            for column in range(9):
                if board[row][column] == '.':
                    continue
                if (board[row][column] in rows[row] or
                        board[row][column] in columns[column] or
                        board[row][column] in boxes[(row // 3, column // 3)]):
                    return False
                rows[row].add(board[row][column])
                columns[column].add(board[row][column])
                boxes[(row // 3, column // 3)].add(board[row][column])
        return True

    def is_valid_sudoku_using_bit_manipulation(self, board: List[List[str]]) -> bool:
        rows = [0] * 9
        columns = [0] * 9
        boxes = [0] * 9
        for row in range(9):
            for column in range(9):
                current = board[row][column]
                if current == '.':
                    continue
                pos = int(current) - 1
                if (rows[row] & (1 << pos) or
                        columns[column] & (1 << pos) or
                        boxes[((row // 3) * 3 + column // 3)] & (1 << pos)):
                    return False
                rows[row] |= (1 << pos)
                columns[column] |= (1 << pos)
                boxes[((row // 3) * 3 + column // 3)] |= (1 << pos)
        return True


board1 = [
    ["5", "3", ".", ".", "7", ".", ".", ".", "."],
    ["6", ".", ".", "1", "9", "5", ".", ".", "."],
    [".", "9", "8", ".", ".", ".", ".", "6", "."],
    ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
    ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
    ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
    [".", "6", ".", ".", ".", ".", "2", "8", "."],
    [".", ".", ".", "4", "1", "9", ".", ".", "5"],
    [".", ".", ".", ".", "8", ".", ".", "7", "9"]
]
print("Board 1 - Is valid sudoku? (HashSet) : " +
      str(ValidSudoku().is_valid_sudoku_using_hashset(board1)))
print("Board 1 - Is valid sudoku? (Bit Manipulation) : " +
      str(ValidSudoku().is_valid_sudoku_using_bit_manipulation(board1)))
print()
board2 = [
    ["8", "3", ".", ".", "7", ".", ".", ".", "."],
    ["6", ".", ".", "1", "9", "5", ".", ".", "."],
    [".", "9", "8", ".", ".", ".", ".", "6", "."],
    ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
    ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
    ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
    [".", "6", ".", ".", ".", ".", "2", "8", "."],
    [".", ".", ".", "4", "1", "9", ".", ".", "5"],
    [".", ".", ".", ".", "8", ".", ".", "7", "9"]
]
print("Board 2 - Is valid sudoku? (HashSet) : " +
      str(ValidSudoku().is_valid_sudoku_using_hashset(board2)))
print("Board 2 - Is valid sudoku? (Bit Manipulation) : " +
      str(ValidSudoku().is_valid_sudoku_using_bit_manipulation(board2)))
