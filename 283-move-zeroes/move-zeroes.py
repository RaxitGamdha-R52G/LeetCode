class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        v = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[v], nums[i] = nums[i], nums[v]
                v += 1

        
        