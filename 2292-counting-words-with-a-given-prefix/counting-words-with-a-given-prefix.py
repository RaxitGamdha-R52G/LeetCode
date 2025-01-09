class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        result = 0
        for i in words:
            if i.startswith(pref):
                result += 1
        return result
        
        