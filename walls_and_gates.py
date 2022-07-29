from collections import deque
from typing import List


class WallsAndGates:
    INF = 2147483647

    def walls_and_gates(self, rooms: List[List[int]]) -> None:
        rows, cols = len(rooms), len(rooms[0])
        q = deque()
        for r in range(rows):
            for c in range(cols):
                if rooms[r][c] == 0:
                    q.append((r, c))
        level = 0
        while q:
            level += 1
            for _ in range(len(q)):
                directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
                cur_r, cur_c = q.popleft()
                for dr, dc in directions:
                    new_r, new_c = cur_r + dr, cur_c + dc
                    if (new_r in range(rows) and
                            new_c in range(cols) and
                            rooms[new_r][new_c] == self.INF and
                            (new_r, new_c) not in q):
                        q.append((new_r, new_c))
                        rooms[new_r][new_c] = min(rooms[new_r][new_c], level)


input_grid1 = [[2147483647, -1, 0, 2147483647],
               [2147483647, 2147483647, 2147483647, -1],
               [2147483647, -1, 2147483647, -1],
               [0, -1, 2147483647, 2147483647]]
obj = WallsAndGates()
obj.walls_and_gates(input_grid1)
print(f"Shortest distances to gates in grid 1: {input_grid1}")
