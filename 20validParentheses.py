class Solution:
    def isValid(self, s: str) -> bool:
        b = []
        ob = ["(", "{", "["]
        cb = [")", "}", "]"]
        map_close = {
            "(": ")",
            "[": "]",
            "{": "}",
        }

        for c in s:
            print(c)
            if c in cb:
                if b == []:
                    return False
                t = b.pop()
                if t not in map_close or map_close[t] != c:
                    return False
            elif c in ob:
                b.append(c)
            else:
                return False
        if b != []:
            return False
        return True


if __name__ == "__main__":
    s = "()[]{}"
    solution = Solution()
    res = solution.isValid(s)
    print(res)
