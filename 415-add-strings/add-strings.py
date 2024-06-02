class Solution:
    def addStrings(self, num1: str, num2: str) -> str:

        num1_l = len(num1)
        num2_l = len(num2)
        if num1_l > num2_l:
            num2 = '0'*(num1_l-num2_l) + num2
        elif num1_l < num2_l:
            num1 = '0'*(num2_l-num1_l) + num1
        
        carry = 0
        l=[]
        for i in range(len(num1)-1,-1,-1):
            d = int(num1[i])+int(num2[i])+carry
            carry = d//10
            d %= 10
            l.insert(0,str(d))
        if carry > 0:
            l.insert(0,str(carry))
        
        return ''.join(l)




        