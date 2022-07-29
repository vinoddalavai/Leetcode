import heapq
from typing import List


class MinCostToConnectAllPoints:
    def min_cost_connect_points(self, points: List[List[int]]) -> int:
        adj_list = {index: [] for index in range(len(points))}
        for i in range(len(points)):
            x1, y1 = points[i]
            for j in range(i + 1, len(points)):
                x2, y2 = points[j]
                distance = abs(x1 - x2) + abs(y1 - y2)
                adj_list[i].append([distance, j])
                adj_list[j].append([distance, i])

        visited = set()
        min_heap = [[0, 0]]
        heapq.heapify(min_heap)
        result = 0
        while len(visited) < len(points):
            cost, node = heapq.heappop(min_heap)
            if node in visited:
                continue
            result += cost
            visited.add(node)
            for nei_cost, nei in adj_list[node]:
                if nei not in visited:
                    heapq.heappush(min_heap, [nei_cost, nei])
        return result


input_points1 = [[0, 0], [2, 2], [3, 10], [5, 2], [7, 0]]
input_points2 = [[3, 12], [-2, 5], [-4, 1]]
obj = MinCostToConnectAllPoints()
print(f"Cost of Minimum Spanning Tree of graph1: {obj.min_cost_connect_points(input_points1)}")
print(f"Cost of Minimum Spanning Tree of graph2: {obj.min_cost_connect_points(input_points2)}")
