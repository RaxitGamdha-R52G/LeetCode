class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums)-1
        mid = (right+left) // 2

        if not nums:
            return 0

        if nums[mid] == target:
            return mid
        elif nums[mid] > target:
            return self.searchInsert(nums[:mid], target)
        else:
            return mid + 1 + self.searchInsert(nums[mid + 1:], target)