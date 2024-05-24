class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        w=False
        l=[word.isupper(),word.islower(),word[0].isupper() and word[1:].islower()]
        for i in l:
            if i:
                w=w or i
        return w
