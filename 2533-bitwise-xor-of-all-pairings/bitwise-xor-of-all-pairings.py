class Solution:
    def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:
        result = 0
        l1 = len(nums1)
        l2 = len(nums2)

        if l1 % 2:
            for i in nums2:
                result ^= i
        
        if l2 % 2:
            for i in nums1:
                result ^= i
        
        return result

        