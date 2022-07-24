from typing import List


class WordSearch:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])
        path = set()

        def dfs(index: int, row: int, col: int):
            if index == len(word):
                return True
            if (row < 0 or col < 0 or
                    row >= rows or col >= cols or
                    word[index] != board[row][col] or (row, col) in path):
                return False

            path.add((row, col))
            result = (dfs(index + 1, row + 1, col) or
                      dfs(index + 1, row - 1, col) or
                      dfs(index + 1, row, col + 1) or
                      dfs(index + 1, row, col -1))
            path.remove((row, col))
            return result

        for row in range(rows):
            for col in range(cols):
                if dfs(0, row, col):
                    return True
        return False


input_board = [['A', 'B', 'C', 'E'], ['S', 'F', 'C', 'S'], ['A', 'D', 'E', 'E']]
target_word = 'BASF'
print("Found Word: " + str(WordSearch().exist(input_board, target_word)))
