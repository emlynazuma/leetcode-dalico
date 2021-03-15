class Solution:
    def romanToInt(self, s: str) -> int:
        _map = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        last = None
        res = 0
        for c in s:
            if not last:
                last = c
            if _map[c] > _map[last]:
                res -= 2 * _map[last]
            res += _map[c]
            last = c
        return res


if __name__ == "__main__":
    s = "MCMXCIV"
    solution = Solution()
    res = solution.romanToInt(s)
    print(res)
