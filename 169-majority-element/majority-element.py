class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        if not nums:
            return -1
        count = 1
        n = nums[0]

        for i in range(1,len(nums)):
            if nums[i] == n:
                count += 1
            else:
                count -= 1
            if count == 0:
                n = nums[i]
                count = 1
        
        return n

        