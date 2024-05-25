class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        str_result=[i for i in columnTitle]
        result=[ord(i)-64 for i in str_result]

        power=0
        final_result=0
        for i in result[::-1]:
            final_result += i*26**power
            power += 1
        
        return final_result