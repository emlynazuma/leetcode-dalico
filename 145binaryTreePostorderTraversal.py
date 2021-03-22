# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def h(self, root: TreeNode) -> List[int]:
        if root:
            return self.h(root.left) + self.h(root.right) + [root.val]
        return []

    def postorderTraversal(self, root: TreeNode) -> List[int]:
        return self.h(root)
