class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if divisor == 0:
            return None

        n = (dividend > 0) ^ (divisor > 0)

        dividend = abs(dividend)
        divisor = abs(divisor)

        ans = 0
        while dividend >= divisor :
            i = 1
            shift, ml = divisor, 1
            while dividend >= shift << i:
                i += 1
            i -= 1
            dividend -= shift << i
            ans += ml << i
        
        result = -ans if n else ans
        if result > 2**31-1:
            return 2**31-1
        elif result < -2**31:
            return -2**31
        else:
            return result
            

        