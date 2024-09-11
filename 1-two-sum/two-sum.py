class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_s = {}
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in num_s:
                return [num_s[complement], i]
            num_s[nums[i]] = i
        return []