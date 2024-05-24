class Solution:
    def convertToBase7(self, num: int) -> str:
        p=True
        l=[]
        if num==0:
            return str(0)
        elif num<0:
            p=False
            num=-num
        while num:
            l.append(str(num % 7))
            num=num // 7
        
        s=''.join(l[::-1])
        return s if p else '-'+s