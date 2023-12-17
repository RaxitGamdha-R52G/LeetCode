class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        a=[i for i in s]
        b=[i for i in t]

        for i in a:
            if i in b:
                b.remove(i)
        
        return b[0]
        