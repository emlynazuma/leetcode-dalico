class Solution:
    def __init__(self):
        self.m = {}

    def climbStairs(self, n: int) -> int:
        if n in self.m:
            return self.m[n]
        elif n == 1:
            return 1
        elif n == 2:
            return 2
        ans = self.climbStairs(n - 1) + self.climbStairs(n - 2)
        self.m[n] = ans
        return ans


class Solution2:
    def __init__(self):
        self.m = {}

    def climbStairs(self, n: int) -> int:
        self.m[-1] = 0
        self.m[0] = 1
        ans = 1
        for i in range(1, n + 1):
            ans = self.m[i - 1] + self.m[i - 2]
            self.m[i] = ans
        return ans
