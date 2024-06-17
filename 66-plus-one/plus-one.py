class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits = list(map(str,digits))
        s = ''.join(digits)
        s = str(int(s)+1)
        return [int(i) for i in s]
        