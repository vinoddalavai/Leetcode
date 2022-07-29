from typing import List


class GraphValidTree:
    def valid_tree(self, n: int, edges: List[List[int]]) -> bool:
        if not n:
            return True
        visited = set()
        graph = {index: [] for index in range(n)}
        for node, neighbor in edges:
            graph[node].append(neighbor)
            graph[neighbor].append(node)

        def dfs(cur_node: int, previous: int):
            if cur_node in visited:
                return False
            visited.add(cur_node)
            for nei in graph[cur_node]:
                if nei == previous:
                    continue
                if not dfs(nei, cur_node):
                    return False
            return True

        return dfs(0, -1) and n == len(visited)
