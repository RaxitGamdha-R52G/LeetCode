class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        if t == '':
            return 0            
        j = 0
        for i in s:
            if i == t[j]:
                if j == len(t)-1:
                    return 0
                j += 1
        return len(t[j:])