class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        a=len(word1)
        b=len(word2)
        c=abs(a-b)
        d=""

        #  #Solution 1:
        # if c==0:
        #     for i in range(0,a):
        #         d+=word1[i]
        #         d+=word2[i]
        # elif a-b<0:
        #     for i in range(0,a):
        #         d+=word1[i]
        #         d+=word2[i]
            
        #     d+=word2[a:]
        # else:
        #     for i in range(0,b):
        #         d+=word1[i]
        #         d+=word2[i]
            
        #     d+=word1[b:]
        # return d

        #  #Solution 2:
        for i in range(0,a if a-b<=0 else b):
                d+=word1[i]
                d+=word2[i]
        if a-b<0:    
            d+=word2[a:]
        elif a-b>0:
            d+=word1[b:]
        
        return d
        