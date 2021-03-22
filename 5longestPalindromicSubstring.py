class Solution:
    def findPalindrome(self, s: str, p: int, q: int) -> str:
        length = len(s)
        while p >= 0 and q < length:
            if s[p] != s[q]:
                break
            p -= 1
            q += 1
        return s[p + 1:q]

    def longestPalindrome(self, s: str) -> str:
        length = len(s)

        if length in [0, 1]:
            return s

        res = ''
        for i in range(length):
            odd = self.findPalindrome(s, i, i)
            if len(odd) > len(res):
                res = odd

            even = self.findPalindrome(s, i, i + 1)
            if len(even) > len(res):
                res = even
        return res


if __name__ == "__main__":
    s = "bbabb"
    solution = Solution()
    res = solution.longestPalindrome(s)
    print(res)
