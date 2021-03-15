from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        for i, r in enumerate(nums):
            s = i
            e = len(nums) - 1
            while e > s:
                if i == e:
                    e -= 1
                elif nums[s] + nums[e] + r == 0:
                    res.append([r, nums[s], nums[e]])
                    s += 1
                elif nums[s] + nums[e] + r == 0:
                    e -= 1
                else:
                    s += 1
        return res


if __name__ == "__main__":
    s = [-1, 0, 1, 2, -1, -4]
    solution = Solution()
    res = solution.threeSum(s)
    print(res)
