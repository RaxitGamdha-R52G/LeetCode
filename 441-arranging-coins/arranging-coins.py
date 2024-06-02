class Solution:
    def arrangeCoins(self, n: int) -> int:
        i = 1
        while True:
            n -= i
            if n < 0:
                return i-1
            elif n == 0:
                return i
            i+=1

        