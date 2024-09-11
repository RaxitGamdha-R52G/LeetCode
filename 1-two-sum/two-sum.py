class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_s = {}
        for i in range(len(nums)):
            if target - nums[i] in num_s:
                return [num_s[target - nums[i]], i]
            num_s[nums[i]] = i
        return [-1,-1]