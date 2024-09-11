class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        N1 = len(nums1)
        N2 = len(nums2)

        N = nums1 if N1 < N2 else nums2
        N3 = nums2 if N1 < N2 else nums1

        i = 0
        while i < len(N):
            if N[i] not in N3:
                N.pop(i)
            else:
                N3.remove(N[i])
                i += 1
        
        return N