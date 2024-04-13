class Solution:
    def reverse(self, x: int) -> int:
        a=str(x)
        c=int(a[::-1] if x>=0 else a[0]+a[:0:-1])
        return c if c>=-2**31 and c<2**31 else 0
        