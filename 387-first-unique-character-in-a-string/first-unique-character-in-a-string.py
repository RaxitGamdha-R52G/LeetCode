class Solution:
    def firstUniqChar(self, s: str) -> int:
        from collections import Counter
        d= Counter(s)
        for i in d:
            if d[i] == 1:
                return s.find(i)

        return -1        