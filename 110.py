# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.res = True

    def height(self, node: TreeNode) -> int:
        if not node:
            return 0
        left = self.height(node.left)
        right = self.height(node.right)
        if abs(left - right) > 1:
            self.res = False
        return max(left, right) + 1

    def isBalanced(self, root: TreeNode) -> bool:
        self.height(root)
        return self.res
