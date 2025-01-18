class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 1
        length = len(digits)
        i = length-1
        while 0 <= i < length :
            if digits[i] == 9:
                digits[i] = 0
            else:
                digits[i] += 1
                return digits
            i -= 1
        
        return [carry] + digits
        