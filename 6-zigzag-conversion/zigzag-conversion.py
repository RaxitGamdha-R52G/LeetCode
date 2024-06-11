class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows < 1:
            return ''
        elif numRows == 1:
            return s
        currentrow = 0
        d = 1
        result = ['']*numRows
        for i in s:
            result[currentrow] += i
            if currentrow == 0:
                d = 1
            if currentrow > 0 and currentrow + 1 == numRows:
                d = -1
            currentrow += d
        return ''.join(result)
        