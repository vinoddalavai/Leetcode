from typing import List


class RedundantConnection:
    def find_redundant_connection(self, edges: List[List[int]]) -> List[int]:
        parent = [index for index in range(len(edges) + 1)]
        rank = [1] * (len(edges) + 1)

        def find(node: int) -> int:
            par = parent[node]
            while par != parent[par]:
                par = parent[parent[par]]
            return par

        def union(node1: int, node2: int) -> bool:
            par1, par2 = find(node1), find(node2)
            if par1 == par2:
                return False
            if rank[par1] > rank[par2]:
                parent[par2] = par1
                rank[par1] += rank[par2]
            else:
                parent[par1] = par2
                rank[par2] += rank[par1]
            return True

        for node1, node2 in edges:
            if not union(node1, node2):
                return [node1, node2]
        return []


input_edges1 = [[1, 2], [1, 3], [2, 3]]
input_edges2 = [[1, 2], [2, 3], [3, 4], [1, 4], [1, 5]]
obj = RedundantConnection()
print(f"Redundant connection in graph1: {obj.find_redundant_connection(input_edges1)}")
print(f"Redundant connection in graph2: {obj.find_redundant_connection(input_edges2)}")
