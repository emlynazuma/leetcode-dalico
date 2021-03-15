class Solution:
    def reverse(self, x: int) -> int:
        if x == 0:
            return 0

        neg = False
        if x < 0:
            x = -x
            neg = True

        res = []
        while x != 0:
            q = x // 10
            r = x % 10
            res.append(r)
            x = q
        _len = len(res)
        out = 0
        for i, item in enumerate(res):
            out += item * (10 ** (_len - i - 1))

        if out > 2 ** 31:
            out = 0

        if neg:
            out = -out
        return out


if __name__ == "__main__":
    s = Solution()
    r = s.reverse(1)
    print(r)
