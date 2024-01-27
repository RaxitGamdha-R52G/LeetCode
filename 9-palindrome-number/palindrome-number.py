class Solution:
    def isPalindrome(self, x: int) -> bool:
        # j=0
        # if x<0:
        #     j=1
        #     x=abs(x)
        
        # k=x
        # d=0
        # while k!=0:
        #     f=k%10
        #     d=10*d+f
        #     k//=10
        
        # if j==1:
        #     d=-d

        x=str(x)
        d=x[::-1]
        
        return True if d==x else False
        