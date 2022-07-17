from typing import List, Optional

from tree_node import TreeNode


class ConstructBinaryTreeFromPreorderAndInorderTraversal:
    def build_tree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return None

        root = TreeNode(preorder[0])
        mid = inorder.index(preorder[0])
        root.left = self.build_tree(preorder[1:mid + 1], inorder[:mid])
        root.right = self.build_tree(preorder[mid + 1:], inorder[mid + 1:])
        return root
