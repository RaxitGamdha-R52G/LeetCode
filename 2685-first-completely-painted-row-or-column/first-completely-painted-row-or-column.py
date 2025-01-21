class Solution:
    def firstCompleteIndex(self, arr: List[int], mat: List[List[int]]) -> int:
        pos = {}
        m = len(mat)
        n = len(mat[0])

        for i in range(m):
            for j in range(n):
                pos[mat[i][j]] = (i,j)

        row = [n] * m
        col = [m] * n

        
        for k in range(len(arr)):
            i, j  = pos[arr[k]]
            row[i] -= 1
            if not row[i]:
                return k
            col[j] -= 1
            if not col[j]:
                return k
        
        return -1