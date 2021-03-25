class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return
        stack = [(root.left, root.right)]

        while stack:
            l, r = stack.pop()
            if not l and not r:
                continue
            elif (l and r) and (l.val == r.val):
                stack.append((l.left, r.right))
                stack.append((l.right, r.left))
            else:
                return False
        return True
