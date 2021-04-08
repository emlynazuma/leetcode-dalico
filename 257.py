# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def h(self, node: TreeNode, pre: List):
        left = node.left
        right = node.right
        if left:
            self.h(left, pre + [left.val])
        if right:
            self.h(right, pre + [right.val])
        if not left and not right:
            self.res.append("->".join(map(str, pre)))

    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        self.res = []
        if not root:
            return self.res
        self.h(root, [root.val])
        return self.res
