class Solution:
    def countSegments(self, s: str) -> int:
        if s:
            start = 0
            count = 0
            for i in range(1, len(s)):
                if s[i] == " " and s[i-1] !=  " ":
                    count += 1
            if s[-1] != " ":
                count += 1
            return count
        return 0
        
        
        