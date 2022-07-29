from typing import List


class ConnectedComponents:
    def count_components(self, n: int, edges: List[List[int]]) -> int:
        parent = [index for index in range(n)]
        rank = [1] * n
        count = n

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
            if union(node1, node2):
                count -= 1
        return count


input_edges1 = [[0, 1], [1, 2], [3, 4]]
input_edges2 = [[0, 1], [1, 2], [2, 3], [3, 4]]
total_edges = 5
obj = ConnectedComponents()
print(f"Total connected components in graph 1: {obj.count_components(total_edges, input_edges1)}")
print(f"Total connected components in graph 1: {obj.count_components(total_edges, input_edges2)}")
