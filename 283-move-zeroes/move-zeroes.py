class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        if len(nums)> 1:
            i = 0
            for j in range(1,len(nums)):
                if nums[i] != 0:
                    i+=1
                if nums[j] != 0 and nums[i] == 0:
                    nums[i],nums[j] = nums[j],nums[i]
                    i+=1
                
            
        