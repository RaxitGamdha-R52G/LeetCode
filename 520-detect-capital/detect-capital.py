class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        # w=False
        # l=[word.isupper(),word.islower(),word==word.capitalize()]
        # for i in l:
        #     if i:
        #         w=w or i
        # return w
        return word.isupper() or word.islower() or word.istitle()