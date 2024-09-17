class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        from collections import Counter
        result = []

        d = Counter((s1+" "+s2).split())
        
        for i in d:
            if d[i] == 1:
                result.append(i)
        
        return result