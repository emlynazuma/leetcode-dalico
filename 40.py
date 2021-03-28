from typing import List


class Solution:
    def __init__(self):
        self.res = []

    def search(self, candidates: List[int], target: int, tmp: List[int], start: int):
        if target == 0:
            self.res.append(tmp[:])
            return
        for i in range(start, len(candidates)):
            if candidates[i] > target:
                return
            if i > start and candidates[i] == candidates[i - 1]:
                continue
            tmp.append(candidates[i])
            self.search(candidates, target - candidates[i], tmp, i + 1)
            tmp.pop()

    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        self.search(candidates, target, [], 0)
        return self.res
