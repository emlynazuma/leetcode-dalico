from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        count = 0
        i = 0
        for _ in range(len(nums)):
            if nums[i] == val:
                del nums[i]
                continue
            count += 1
            i += 1
        return count
