class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        a=[]
        b=[]
        for i in s:
            a.append(i)
        for j in t:
            b.append(j)
        a.sort()
        b.sort()
        if a==b:
            return True
        else:
            return False
        