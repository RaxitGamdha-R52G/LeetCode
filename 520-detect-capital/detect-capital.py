class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        w=False
        if word.isupper():
            w=w or True
        if word.islower():
            w=w or True
        if word[0].isupper() and word[1:].islower():
            w= w or True
        return w
