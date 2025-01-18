class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        no = {
            '2':'abc',
            '3':'def',
            '4':'ghi',
            '5':'jkl',
            '6':'mno',
            '7':'pqrs',
            '8':'tuv',
            '9':'wxyz'
        }
        
        n = len(digits)
        result = []
        def backtrack(temp, curr):
            if curr == n :
                result.append(temp)
                return
            for i in digits[curr]:
                for char in no[i]:
                    backtrack(temp + char, curr + 1)
        
        backtrack("", 0)
        return result