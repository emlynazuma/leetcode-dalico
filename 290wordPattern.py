class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        _s = s.split(" ")

        if len(pattern) != len(_s):
            return False

        seen = {}
        seen_r = {}
        for p, c in zip(pattern, _s):
            if p not in seen:
                seen[p] = c
            if c not in seen_r:
                seen_r[c] = p
            if seen[p] != c or seen_r[c] != p:
                return False
        return True
