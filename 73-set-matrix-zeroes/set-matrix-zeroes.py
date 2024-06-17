class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        if matrix:
            d = False
            right = len(matrix)-1
            n = len(matrix[0])
            left = 0
            mid_a = 0
            a = []
            while left <= right:
                if d:
                    for i in range(n):
                        if matrix[mid_a][i] == 0:
                            a.append(i)
                        else:
                            matrix[mid_a][i] = 0
                    left = mid_a+1
                    right = len(matrix)-1
                    d = False                   
                    
                elif 0 in matrix[left]:
                    mid_a = left
                    left = 0
                    d = True
                    right = n-1
                else:
                    left += 1
                
            for i in range(len(matrix)):
                for j in a:
                    matrix[i][j] = 0

                
                