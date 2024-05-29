class Solution:
    def minOperations(self, nums: List[int]) -> int:
        total_operations = 0
        from collections import Counter
        nums= Counter(nums)
        for i in nums:
            while nums[i]>0:
                if nums[i] > 1:
                    if nums[i] % 3 ==0  and nums[i] % 2 == 0 or (nums[i] % 3 in [0,2] and nums[i] != 2):
                        nums[i] -= 3 
                    else:
                        nums[i] -= 2
                    total_operations += 1
                elif nums[i]==1:
                    return -1
        return total_operations
                


