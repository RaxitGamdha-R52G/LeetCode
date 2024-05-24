class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        import math
        d=sum((i if i== num//i else i+num//i for i in range(1,int(math.sqrt(num))+1) if num%i==0))
        return d==num*2 and num != 1