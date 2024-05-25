class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        # k=[[1]*(i+1) for i in range(rowIndex+1)]

        # for i in range(len(k)):
        #     for j in range(len(k[i])):
        #         if j ==0 or j== len(k[i])-1:
        #             continue
        #         k[i][j]=k[i-1][j-1]+k[i-1][j]
        
        # return k[len(k)-1]
        import math

        return [math.comb(rowIndex,i) for i in range(rowIndex +1)]