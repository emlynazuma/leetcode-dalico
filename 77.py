from typing import List


class Solution:
    def __init__(self):
        self.ans = []

    def h(self, loop: int, last: int, res: List[List[int]]):
        if loop == self.k:
            self.ans.append(res[:])
            return
        for j in range(last, self.n):
            self.h(loop + 1, j + 1, res + [j + 1])

    def combine(self, n: int, k: int) -> List[List[int]]:
        self.n = n
        self.k = k
        self.h(loop=0, last=0, res=[])
        return self.ans
