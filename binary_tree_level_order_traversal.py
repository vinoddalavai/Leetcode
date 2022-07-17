import collections
from typing import Optional, List

from tree_node import TreeNode


class BinaryTreeLevelOrderTraversal:
    def level_order(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        q = collections.deque([root])
        result = []
        while q:
            level_result = []
            for index in range(len(q)):
                node = q.popleft()
                level_result.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            result.append(level_result)