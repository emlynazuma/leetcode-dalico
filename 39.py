from typing import List


class Solution:
    def __init__(self):
        self.res = []

    def search(self, candidates: List[int], target: int, sub: List[int], last: int):
        if target == 0:
            self.res.append(sub[:])
            return
        for n in candidates:
            if n > target:
                return
            if n < last:
                continue
            sub.append(n)
            self.search(candidates, target - n, sub, n)
            sub.pop()

    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        self.search(candidates, target, [], 0)
        return self.res
