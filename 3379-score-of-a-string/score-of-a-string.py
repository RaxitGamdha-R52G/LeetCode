class Solution:
    def scoreOfString(self, s: str) -> int:
        v = 0
        for i in range(1,len(s)):
            v += abs(ord(s[i])-ord(s[i-1]))
        return v
        