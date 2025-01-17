class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        s_l = set(len(i) for i in strs)
        ms = min(s_l)
        result = ''
        temp = strs[0]
        for i in range(0,ms):
            for j in strs:
                if temp[i] != j[i]:
                    return result
            
            result += temp[i]
        return result