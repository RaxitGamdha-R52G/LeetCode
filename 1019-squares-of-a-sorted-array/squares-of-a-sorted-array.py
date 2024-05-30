class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        d = [i**2 for i in nums]
        d.sort()
        return d