from typing import Optional
from tree_node import TreeNode


class InvertBinaryTree:
    def invert_tree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        left, right = self.invert_tree(root.left), self.invert_tree(root.right)
        root.left, root.right = right, left
        return root
