class Solution:
    def romanToInt(self, s: str) -> int:
        a={
            "I":1,
            "V":5,
            "X":10,
            "L":50,
            "C":100,
            "D":500,
            "M":1000,
        }
        c=0
        S = len(s)
        i = 0
        while i < S:
            if i < S - 1 and a[s[i]] < a[s[i + 1]]:
                c += a[s[i + 1]] - a[s[i]]
                i += 2
            else:
                c += a[s[i]]
                i += 1

        return c
        