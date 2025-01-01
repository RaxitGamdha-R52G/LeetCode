class Solution:
    def maxScore(self, s: str) -> int:
        if s == '':
            return 0
        result = float('-inf')
        for i in range(1,len(s)):
            left = s[:i]
            right = s[i:]
            l_c = r_c = 0
            for i in left:
                if i == '0':
                    l_c += 1
            
            for i in right:
                if i == '1':
                    r_c += 1
            
            temp = l_c + r_c
            if temp > result:
                result = temp
        
        return result