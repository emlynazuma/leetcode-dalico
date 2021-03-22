import heapq
from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        res = nums[:k]
        heapq.heapify(res)
        for num in nums[k:]:
            heapq.heappushpop(res, num)
        return res[0]
