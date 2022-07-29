from typing import List


class PacificAtlanticWaterFlow:
    def pacific_atlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows, columns = len(heights), len(heights[0])
        result = []
        pacific, atlantic = set(), set()

        def dfs(row: int, col: int, visited: set, previous_height: int) -> None:
            if (row not in range(rows) or
                    col not in range(columns) or
                    (row, col) in visited or
                    heights[row][col] < previous_height):
                return

            visited.add((row, col))
            directions = [
                [1, 0],  # move right
                [-1, 0],  # move left
                [0, 1],  # move up
                [0, -1]  # move down
            ]
            for dr, dc in directions:
                dfs(row + dr, col + dc, visited, heights[row][col])

        for c in range(columns):
            dfs(0, c, pacific, heights[0][c])
            dfs(rows - 1, c, atlantic, heights[rows - 1][c])
        for r in range(rows):
            dfs(r, 0, pacific, heights[r][0])
            dfs(r, columns - 1, atlantic, heights[r][columns - 1])

        for r in range(rows):
            for c in range(columns):
                if (r, c) in atlantic and (r, c) in pacific:
                    result.append([r, c])
        return result


input_heights1 = [[1, 2, 2, 3, 5], [3, 2, 3, 4, 4], [2, 4, 5, 3, 1], [6, 7, 1, 4, 5], [5, 1, 1, 2, 4]]
input_heights2 = [[2, 1], [1, 2]]
print("List of cells that can empty into both Atlantic and Pacific:")
obj = PacificAtlanticWaterFlow()
print(f"\t From first input: {obj.pacific_atlantic(input_heights1)}")
print(f"\t From second input: {obj.pacific_atlantic(input_heights2)}")
