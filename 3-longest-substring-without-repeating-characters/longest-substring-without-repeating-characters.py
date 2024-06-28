class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        if n == 0:return 0
        length = 0
        c_set = set()
        left = 0
        for right in range(n):
            while s[right] in c_set:
                c_set.remove(s[left])
                left += 1
            c_set.add(s[right])
            length = max(length, right-left+1)
        return length 