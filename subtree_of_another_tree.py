from typing import Optional

import same_tree
from tree_node import TreeNode


class SubtreeOfAnotherTree:
    def is_subtree(self, root: Optional[TreeNode], sub_root: Optional[TreeNode]) -> bool:
        if not sub_root:
            return True
        if not root:
            return False

        if same_tree.SameTree().is_same_tree(root, sub_root):
            return True
        else:
            return self.is_subtree(root.left, sub_root) or self.is_subtree(root.right, sub_root)