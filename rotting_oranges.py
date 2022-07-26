from collections import deque
from typing import List


class RottingOranges:
    def oranges_rotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        q = deque()
        time = -1

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    q.append((r, c))

        if not q:
            for r in range(rows):
                for c in range(cols):
                    if grid[r][c] == 1:
                        return time
            return 0

        while q:
            time += 1
            for _ in range(len(q)):
                cur_row, cur_col = q.popleft()
                directions = [
                    [1, 0],
                    [-1, 0],
                    [0, 1],
                    [0, -1]
                ]
                for dr, dc in directions:
                    if (cur_row + dr in range(rows) and
                            cur_col + dc in range(cols) and
                            grid[cur_row + dr][cur_col + dc] == 1):
                        grid[cur_row + dr][cur_col + dc] = 2
                        q.append((cur_row + dr, cur_col + dc))

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    return -1

        return time


input_grid = [[2, 1, 1], [1, 1, 0], [0, 1, 1]]
obj = RottingOranges()
print(f"Time taken for all oranges to rot: {obj.oranges_rotting(input_grid)}")
