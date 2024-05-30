class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        min_num = float('inf')
        for i in range(1,len(matrix)):
            d = len(matrix[i])
            for j in range(d):
                v=[]
                if j-1>=0:
                    v.append(matrix[i-1][j-1])
                v.append(matrix[i-1][j])
                if j+1<d:
                    v.append(matrix[i-1][j+1])
                matrix[i][j] += min(v)
        return min(matrix[len(matrix)-1])