# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.res = []

    def h(self, root: TreeNode):
        if not root:
            return
        self.h(root.left)
        self.res.append(root.val)
        self.h(root.right)

    def kthSmallest(self, root: TreeNode, k: int) -> int:
        self.h(root)
        return self.res[k - 1]
