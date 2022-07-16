from typing import Optional
from tree_node import TreeNode


class BalancedBinaryTree:
    def is_balance(self, root: Optional[TreeNode]) -> bool:
        def depth(node):
            if not node:
                return True, 0
            left, right = depth(node.left), depth(node.right)
            balanced = left[0] and right[0] and abs(left[1] - right[1]) <= 1
            return balanced, 1 + max(left[1], right[1])
        return depth(root)[0]