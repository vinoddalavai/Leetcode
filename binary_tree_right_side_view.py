from collections import deque
from typing import Optional, List
from tree_node import TreeNode


class BinaryTreeRightSideView:
    def right_side_view(self, root: Optional[TreeNode]) -> List[int]:
        if not root: return []

        result = []
        q = deque([root])
        while q:
            q_length = len(q)
            for index in range(len(q)):
                node = q.popleft()
                if index == (q_length - 1):
                    result.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
        return result