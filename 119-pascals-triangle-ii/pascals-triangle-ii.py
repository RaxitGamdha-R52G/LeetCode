class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        import math
        return [math.comb(rowIndex,i) for i in range(rowIndex +1)]