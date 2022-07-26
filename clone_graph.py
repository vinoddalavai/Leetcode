class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class CloneGraph:
    def clone_graph(self, node: 'Node') -> 'Node':
        original_to_clone = {}

        def dfs(vertex: 'Node'):
            if vertex in original_to_clone:
                return original_to_clone[vertex]

            clone_node = Node(vertex.val)
            original_to_clone[vertex] = clone_node
            for neighbor in vertex.neighbors:
                clone_node.neighbors.append(dfs(neighbor))
            return clone_node

        return dfs(node) if node else None


node1, node2, node3, node4 = Node(1), Node(2), Node(3), Node(4)
node1.neighbors.extend([node2, node4])
node2.neighbors.extend([node1, node3])
node3.neighbors.extend([node2, node4])
node4.neighbors.extend([node1, node3])
test = CloneGraph()
res = test.clone_graph(node1)
print(res)
