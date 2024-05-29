class Solution:
    def minOperations(self, nums: List[int]) -> int:
        total_operations=0
        import math
        for value in Counter(nums).values():
            if value == 1: return -1
            total_operations += math.ceil(value / 3)
        return total_operations
                


