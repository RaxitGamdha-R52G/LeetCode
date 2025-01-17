class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        # Solution 1
        # left_min = 1
        # hmap = defaultdict(int)
        # for i in nums:
        #     if i > 0:
        #         hmap[i] = 1
        #         while hmap[left_min] > 0:
        #             del hmap[left_min]
        #             left_min += 1
        # return left_min

        # Solution 2
        n = len(nums)
        for i in range(n):
            while 1 <= nums[i] <= n and nums[i] != nums[nums[i] - 1]:
                nums[nums[i] -1], nums[i] = nums[i], nums[nums[i] -1]
        
        for i in range(n):
            if nums[i] != i + 1:
                return i + 1
        
        return n + 1
        