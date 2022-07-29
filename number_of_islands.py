from typing import List


class NumberOfIslands:
    def num_islands(self, grid: List[List[str]]) -> int:
        rows, columns = len(grid), len(grid[0])
        visited = set()
        result = 0

        def dfs(row: int, column: int) -> None:
            if (
                    row not in range(rows) or
                    column not in range(columns) or
                    (row, column) in visited or
                    grid[row][column] == '0'
            ):
                return

            visited.add((row, column))
            directions = [
                [0, 1],     # move right
                [0, -1],    # move left
                [-1, 0],    # move down
                [1, 0]      # move up
            ]
            for r, c in directions:
                dfs(row + r, column + c)

        for row in range(rows):
            for column in range(columns):
                if grid[row][column] == '1' and (row, column) not in visited:
                    result += 1
                    dfs(row, column)

        return result


input_grid1 = [
    ["1", "1", "1", "1", "0"],
    ["1", "1", "0", "1", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "0", "0", "0"]
]
input_grid2 = [
    ["1", "1", "0", "0", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "1", "0", "0"],
    ["0", "0", "0", "1", "1"]
]
obj = NumberOfIslands()
print(f"Number of islands on Grid 1 = {obj.num_islands(input_grid1)}")
print(f"Number of islands on Grid 2 = {obj.num_islands(input_grid2)}")
