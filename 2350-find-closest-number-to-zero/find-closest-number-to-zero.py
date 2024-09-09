class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        closest = nums[0]
        for i in nums:
            if abs(i) < abs(closest):
                closest = i

        return abs(closest) if closest < 0 and abs(closest) in nums else closest
        