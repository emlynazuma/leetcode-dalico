class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        num1 = [int(s) for s in num1]
        num2 = [int(s) for s in num2]
        res = []
        c = 0

        while num1 and num2:
            d = num1.pop() + num2.pop() + c
            if d > 9:
                d -= 10
                c = 1
            else:
                c = 0
            res.append(str(d))

        t = num1 or num2

        while t:
            d = t.pop() + c
            if d > 9:
                d -= 10
                c = 1
            else:
                c = 0
            res.append(str(d))
        if c == 1:
            res = res + ['1']
        c = 0
        res.reverse()
        return ''.join(res)


if __name__ == "__main__":
    s1 = "123456789"
    s2 = "987654321"

    solution = Solution()

    solution.addStrings(s1, s2)
