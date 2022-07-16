from typing import Optional

from tree_node import TreeNode


class SameTree:
    def is_same_tree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        if p and q and p.val == q.val:
            return (self.is_same_tree(p.left, q.left) and self.is_same_tree(p.right, q.right))
        else:
            return False