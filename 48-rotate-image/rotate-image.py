class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        v = len(matrix)

        for i in range(v-1):
            for j in range(i+1,v):
                matrix[i][j],matrix[j][i] = matrix[j][i],matrix[i][j]
            

        for i in range(v):
            for j in range(v//2):
                matrix[i][j],matrix[i][v-1-j]=matrix[i][v-1-j],matrix[i][j]
        
        
        