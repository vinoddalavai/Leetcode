from typing import Optional
from tree_node import TreeNode


class MaximumDepthOfABinaryTree:
    def max_depth(self, root: Optional[TreeNode]):
        if not root:
            return 0
        return max(1 + self.max_depth(root.left), 1 + self.max_depth(root.right))
