class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        if n == 0:
            return ['']
        result = []
        
        def backtrack(temp, open_p, close_p):
            if len(temp) == 2 * n:
                result.append(temp)
                return
            if open_p < n:
                backtrack(temp + "(", open_p + 1, close_p)
            if close_p < open_p:
                backtrack(temp + ")", open_p, close_p + 1)
            
        backtrack("", 0, 0)
        return result