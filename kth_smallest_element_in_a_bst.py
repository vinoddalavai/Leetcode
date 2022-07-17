from typing import Optional

from tree_node import TreeNode


class KthSmallestElementInABst:
    def kth_smallest(self, root: Optional[TreeNode], k: int) -> int:

        def dfs(node):
            result = []
            if not node:
                return result
            left = dfs(node.left)
            result.append(node.val)
            right = dfs(node.right)
            return left + result + right

        result = dfs(root)
        return result[k - 1]
