class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        if len(digits)==0 :
            return []
        else:
            c=1
            for i in range(len(digits)-1,-1,-1):
                digits[i]+=c
                if digits[i]<10:
                    c=0
                else:
                    digits[i]=0
                    c=1
            
            if c==1:
                digits.insert(0,1)
            return  digits
                
                