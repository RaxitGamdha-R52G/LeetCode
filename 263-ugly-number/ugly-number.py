class Solution:
    def isUgly(self, n: int) -> bool:
        for i in (2,3,5):
            while n:
                if n % i == 0:
                    n = n // i
                else:
                    break
        
        return True if n == 1 else False

        
            
            
        