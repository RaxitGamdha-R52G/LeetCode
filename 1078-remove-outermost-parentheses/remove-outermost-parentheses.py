class Solution:
    def removeOuterParentheses(self, s: str) -> str:
    
        length = 0
        result = ""
        for i in s:
            if i == "(":
                if length > 0:
                    result += i
                length += 1
            else:
                length -= 1
                if length > 0:
                    result += i
        return result