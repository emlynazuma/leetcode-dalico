class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        _max = 0
        seen = []
        for c in s:
            if c in seen:
                r = seen.index(c)
                seen = seen[r + 1:]
            seen.append(c)
            length = len(seen)

            if length > _max:
                _max = length
        return _max
