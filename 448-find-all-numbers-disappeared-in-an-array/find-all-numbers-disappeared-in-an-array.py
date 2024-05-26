class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        nums_l=set([i for i in range(1,len(nums)+1)])
        nums=set(nums)
        return list(nums_l-nums)
        