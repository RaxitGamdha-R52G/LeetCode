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

        i = 0
        while i < len(s) - 1:
            if a[s[i]] < a[s[i + 1]]:
                c += a[s[i + 1]] - a[s[i]]
                i += 2
            else:
                c += a[s[i]]
                i += 1

        if i < len(s):
            c += a[s[i]]

        return c
            