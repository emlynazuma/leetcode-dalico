from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []

        ready = [root]
        next_level = []
        t = []
        res = []
        while True:
            if ready:
                c = ready.pop(0)
                if c:
                    t.append(c.val)
                    next_level.append(c.left)
                    next_level.append(c.right)
            elif next_level:
                res.append(t)
                t = []
                ready = next_level
                next_level = []
            else:
                break
        return res
