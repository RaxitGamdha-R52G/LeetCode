class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        from itertools import permutations
        per_arr = list(permutations(nums))
        result = list(map(list,per_arr))
        return result
        