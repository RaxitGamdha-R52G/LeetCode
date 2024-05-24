class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        result=[]
        while columnNumber > 0:
            columnNumber-= 1
            result.insert(0,chr(65+columnNumber %26))
            columnNumber //= 26
        return ''.join(result) 
        
