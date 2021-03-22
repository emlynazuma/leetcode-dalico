from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        tmp = {}
        for n in nums:
            if n in tmp:
                tmp.pop(n)
                continue
            tmp[n] = 1
        return list(tmp.keys())[0]


class Solution2:
    def singleNumber(self, nums: List[int]) -> int:
        ans = 0
        for num in nums:
            ans ^= num
        return ans


if __name__ == "__main__":
    nums = [4, 1, 2, 1, 2]
    solution = Solution()
    res = solution.singleNumber(nums)
    print(res)
