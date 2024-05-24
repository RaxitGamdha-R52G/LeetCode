class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        l=0
        for i in nums:
            l = l ^ i
        return l