from tree_node import TreeNode


class CountGoodNodesInBinaryTree:
    def good_nodes(self, root: TreeNode) -> int:
        
        def dfs(node: TreeNode, max_value: int) -> int:
            if not node:
                return 0
            result = 1 if node.val >= max_value else 0
            max_value = max(max_value, node.val)
            result += dfs(node.left, max_value)
            result += dfs(node.right, max_value)
            return result

        return dfs(root, root.val)
