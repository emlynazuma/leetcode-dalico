from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits[-1] += 1
        digits.reverse()
        c = 0
        res = []
        for d in digits:
            s = d + c
            if s > 10:
                s -= 10
                c = 1
            else:
                c = 0
            res.append(s)
        if res[0] > 10:
            res[0] -= 10
            res = [1] + res
        res.reverse()
        return res
