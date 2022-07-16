from typing import Optional
from tree_node import TreeNode


class DiameterOfBinaryTree:
    diameter = 0
    def diameter_of_binary_tree(self, root: Optional[TreeNode]) -> int:
        def depth(node: Optional[TreeNode]):
            if not node:
                return -1
            left, right = 1 + depth(node.left), 1 + depth(node.right)
            self.diameter = max(self.diameter, left + right)
            return max(left, right)
        depth(root)
        return self.diameter
