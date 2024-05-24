class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        l=0
        for i in nums:
            l = l ^ i
        return l