class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        a=len(word1)
        b=len(word2)
        c=abs(a-b)
        d=""
        if c==0:
            for i in range(0,a):
                d+=word1[i]
                d+=word2[i]
        elif a-b<0:
            for i in range(0,a):
                d+=word1[i]
                d+=word2[i]
            
            d+=word2[a:]
        else:
            for i in range(0,b):
                d+=word1[i]
                d+=word2[i]
            
            d+=word1[b:]
        return d
        