class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        c=0
        g=len(strs[c])
        for i in range(len(strs)):
            if len(strs[i])<g:
                g=len(strs[i])
                c=i
        v=0
        f=""
        k=0
        while v<len(strs[c]):
            d=strs[c][v]
            for i in strs:
                if i[v]!=d:
                    k=1
                    break
            else:
                f+=d
                v+=1

            if k==1:
                return f
        return f