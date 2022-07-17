from typing import Optional

from tree_node import TreeNode


class ValidateBinarySearchTree:
    def is_valid_bst(self, root: Optional[TreeNode]) -> bool:

        def dfs(node, left, right):
            if not node:
                return True
            if node.val <= left or node.val >= right:
                return False
            else:
                return dfs(node.left, left, node.val) and dfs(node.right, node.val, right)

        return dfs(root, float('-inf'), float('inf'))
