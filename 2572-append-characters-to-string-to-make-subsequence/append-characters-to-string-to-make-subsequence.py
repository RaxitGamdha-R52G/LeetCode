class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        if t in s:
            return 0
        # start = 0

        # for i in t:
        #     if i in s[start:]:
        #         index = s.index(i)
        #         start = index+1
        #     else:
        #         id = t.index(i)
        #         d = len(t[id:])
        #         return d
        
        # return 0
            
        j = 0
        for i in s:
            if i == t[j]:
                if j == len(t)-1:
                    return 0
                j += 1
        return len(t[j:])