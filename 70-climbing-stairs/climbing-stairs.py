class Solution:
    def climbStairs(self, n: int) -> int:
        if n < 2:
            return n
        d= [0] * n
        d[0]=1
        d[1] = 2

        for i in range(2,n):
            d[i] = d[i-1] + d[i-2]
        
        return d[n-1]