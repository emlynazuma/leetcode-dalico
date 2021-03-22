from typing import List


class Solutiont:
    def removeDuplicates(self, nums: List[int]) -> int:
        c = None
        for n in nums:
            if n == c:
                nums.remove(n)
            c = n
        return len(nums)


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        last = None
        length = len(nums)
        i = k = 0
        while k < length:
            if nums[i] == last:
                del nums[i]
            else:
                last = nums[i]
                i += 1
            k += 1
