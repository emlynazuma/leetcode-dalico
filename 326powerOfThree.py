class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n <= 0:
            return False

        if n == 1:
            return True

        while n > 1:
            q = n // 3
            r = n % 3
            if r != 0:
                return False
            elif q == 1:
                return True
            n = q
