class Solution:
    def maxArea(self, height: List[int]) -> int:
        p = 0
        q = len(height) - 1
        max_area = 0
        while p < q:
            area = min(height[p], height[q]) * (q - p)
            if area > max_area:
                max_area = area
            if height[p] > height[q]:
                q -= 1
            else:
                p += 1
        return max_area
