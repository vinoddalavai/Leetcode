from typing import List


class MaxAreaOfIsland:
    def max_area_of_island(self, grid: List[List[int]]) -> int:
        rows, columns = len(grid), len(grid[0])
        visited = set()
        max_area = 0

        def dfs(row: int, col: int):
            if (
                row not in range(rows) or
                col not in range(columns) or
                (row, col) in visited or
                grid[row][col] == 0
            ):
                return 0

            cur_area = grid[row][col]
            visited.add((row, col))
            directions = [
                [0, 1],   # move right
                [0, -1],  # move left
                [1, 0],   # move up
                [-1, 0]   # move down
            ]

            for dr, dc in directions:
                cur_area += dfs(row + dr, col + dc)
            return cur_area

        for r in range(rows):
            for c in range(columns):
                if grid[r][c] == 1 and (r, c) not in visited:
                    max_area = max(max_area, dfs(r, c))

        return max_area


input_grid1 = [
    [0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
    [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0],
    [0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0]
]
input_grid2 = [[0, 0, 0, 0, 0, 0, 0, 0]]
obj = MaxAreaOfIsland()
print(f"Max area of island on Grid 1 = {obj.max_area_of_island(input_grid1)}")
print(f"Max area of island on Grid 2 = {obj.max_area_of_island(input_grid2)}")
