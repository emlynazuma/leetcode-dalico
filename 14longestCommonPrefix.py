from typing import List


class Solution2:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if strs == []:
            return ''

        l_ = strs[0]

        for w in strs[1:]:
            _min = min(len(w), len(l_))

            t = ''
            for i in range(_min):
                if w[i] != l_[i]:
                    break
                t += w[i]

            l_ = t

            if not t:
                return t

        return l_


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if strs == []:
            return ''

        l_ = None
        for w in strs:
            if l_ is None:
                l_ = w
                continue
            _min = min(len(w), len(l_))

            t = ''
            for i in range(_min):
                if w[i] != l_[i]:
                    break
                t += w[i]

            l_ = t

            if not t:
                return t

        return l_


if __name__ == "__main__":
    s = ["", "b"]
    solution = Solution()
    res = solution.longestCommonPrefix(s)
    print(res)
