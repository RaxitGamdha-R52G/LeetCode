class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        a=[i for i in s.split(" ") if i!=""]
        return len(a[len(a)-1])
