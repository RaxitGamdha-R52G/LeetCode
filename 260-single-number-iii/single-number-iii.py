class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        b= Counter(nums)
        result = [i for i in b.keys() if b[i]==1]
        return result