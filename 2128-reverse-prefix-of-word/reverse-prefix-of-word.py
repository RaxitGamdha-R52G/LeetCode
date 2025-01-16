class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        index = -1
        result = ""
        for i in range(len(word)):
            if word[i] == ch:
                index = i
                result = word[index::-1]
                break
        result += word[index+1:]
        
        return result
        