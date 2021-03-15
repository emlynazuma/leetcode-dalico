class Solution:

    def lengthOfLongestSubstring(self, s: str) -> int:
        if s == "":
            return 0
        longest = 1
        seen = []
        for c in s:
            if c in seen:
                if len(seen) > longest:
                    longest = len(seen)
                seen = []
            seen.append(c)
        if len(seen) > longest:
            longest = len(seen)
        return longest


if __name__ == "__main__":
    test = "au"
    s = Solution()
    r = s.lengthOfLongestSubstring(test)
    print(r)
