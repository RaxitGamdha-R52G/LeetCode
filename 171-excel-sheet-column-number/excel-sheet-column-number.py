class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        result=0
        power=len(columnTitle)-1
        for i in columnTitle:
            result += (ord(i)-64) * 26 ** power
            power -= 1
        
        return result