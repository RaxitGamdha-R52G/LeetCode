class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        # for i in range(len(nums)):
        #     for j in range(len(nums)-1):
        #         if nums[j]==0:
        #             nums[j],nums[j+1]=nums[j+1],nums[j]
        
        non_zero_index = 0

        # Move all non-zero elements to the front
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[non_zero_index], nums[i] = nums[i], nums[non_zero_index]
                non_zero_index += 1

        
        