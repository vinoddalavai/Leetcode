import sys
from typing import List


class WordSearch:
    def _exist(self, board: List[List[str]], word: str) -> bool:
        """Check is word exists in the board
        Checks for continuous cells horizontally, vertically or a combination of both that form the target word

        Args:
            board (List[List[str]]): M x N board with each cell holding a character value
            word (str): target word to be found in the board

        Returns:
            bool: True if word exists in the board, False otherwise
        """

        rows, columns = len(board), len(board[0])
        visited = set()

        def dfs(row: int, column: int, index: int) -> bool:
            """DFS implementation starting at the position (row, column) to find the target word in the board

            Args:
                row (int): row index to start DFS
                column (int): column index to start DFS
                index (int): current index position of the word whose corresponding character we are trying to find out

            Returns:
                bool: True if character at the current index matches the character of the word at that index
            """

            # base case: if character at index position matches the one in the word at that index return True
            if word[index] == board[row][column]:
                return True
            # base case: if row and column is out of bounds or character at index does not match or if the character on
            # the board has already been visited, return False
            if (
                row < 0 or
                column < 0 or
                row >= rows or
                column >= columns or
                word[index] != board[row][column] or
                (row, column) in visited
            ):
                return False
            
            visited.add((row, column))
            # character matches that of the word at that index so start dfs again from all four neighboring cells
            result = (
                dfs(row, column + 1, index + 1) or
                dfs(row, column - 1, index + 1) or
                dfs(row - 1, column, index + 1) or
                dfs(row + 1, column, index + 1)
            )
            # reset path by removing the cell's value from visited set
            visited.remove((row, column))
            return result
        
        # perform dfs from every cell of the board until the word is found
        for r in range(rows):
            for c in range(columns):
                if dfs(r, c, 0):
                    return True
        return False

    def process(self, board: List[List[int]], word: str) -> None:
        print(f"\nInput: \n\tboard: {board}\ttarget: {word}")
        print(f"\nOutput:\n\t{self._exist(board, word)}\n")

if __name__ == '__main__':
   if len(sys.argv) > 1 and sys.argv[1] == '-d':
       board, word = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "ABCCED"
       WordSearch().process(board, word)
   else:
       num_rows = int(input("Enter number of rows in the board: "))
       num_columns = int(input("Enter number of columns in the board: "))
       board = [[] for _ in range(num_rows)]
       for row in range(num_rows):
           for col in range(num_columns):
               board[row].append(input(f"Enter value at position ({row}, {col}): "))
       target_word = input("Enter target word to find: ")
       WordSearch().process(board, target_word)