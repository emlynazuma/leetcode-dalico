class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        m = {}
        for i, n in enumerate(nums):
            if n not in m:
                m[n] = 1
            elif m[n] == 2:
                m.pop(n)
            else:
                m[n] += 1
        return list(m.keys())[0]