# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.r = []

    def healper(self, c: TreeNode):
        if c is None:
            return
        self.healper(c.left)
        self.r.append(c.val)
        self.healper(c.right)

    def preorderTraversal(self, root: TreeNode) -> List[int]:
        self.healper(root)
        return self.r
