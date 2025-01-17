class Solution:
    def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:
        n1 = 0
        for i in nums1:
            n1 ^= i
        
        n2 = 0
        for i in nums2:
            n2 ^= i
        

        if len(nums1) % 2 == 1 and len(nums2) % 2 == 1:
            return n1 ^ n2
        elif len(nums1) % 2 == 0 and len(nums2) % 2 == 0:
            return 0
        elif len(nums1) % 2 == 1:
            return n2
        else:
            return n1

        