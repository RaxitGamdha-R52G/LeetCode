class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        k=[[0]*(i+1) for i in range(numRows)]
        if numRows==0:
            return []
        else:
            k[0][0]=1
            for i in range(len(k)):
                for j in range(len(k[i])):
                    if j==0 or j==len(k[i])-1:
                        k[i][j]=1
                    else:
                        k[i][j]=k[i-1][j-1]+k[i-1][j]
        
        return k
                    

            
        
        
        