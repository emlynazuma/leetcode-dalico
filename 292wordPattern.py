class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        _s = s.split(" ")

        current_pattern = pattern[0]
        current_s = _s[0]

        for i in range(1, len(pattern)):
            print(current_pattern)
            print(pattern[i])
            print(current_s)
            print(_s[i])
            print(i)
            print((current_pattern == pattern[i]) == (current_s == _s[i]))
            if (current_pattern == pattern[i]) != (current_s == _s[i]):
                return False
            current_pattern = pattern[i]
            current_s = _s[i]
        return True


if __name__ == "__main__":
    pattern = "abba"
    s = "dog cat cat dog"
    solution = Solution()
    res = solution.wordPattern(pattern, s)
    print(res)
