class Solution:
    def tribonacci(self, n: int) -> int:
        if n <= 0:
            return 0
        elif n in (1,2):
            return 1
        a = 0
        b = 1
        c = 1
        for i in range(n-2):
            a,b,c = b,c,a+b+c
        return c
        