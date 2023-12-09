class Solution:
    def arraySign(self, nums: List[int]) -> int:
        m=1
        for i in nums:
            m*=i
        if m==0:
            return 0
        elif m<0:
            return -1
        else:
            return 1