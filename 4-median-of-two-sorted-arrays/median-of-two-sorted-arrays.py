from typing import List

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # Ensure nums1 is the smaller array
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        
        l1, l2 = len(nums1), len(nums2)
        left, right = 0, l1
        
        while left <= right:
            part_X = (left + right) // 2
            part_Y = (l1 + l2 + 1) // 2 - part_X

            maxLeftX = float('-inf') if part_X == 0 else nums1[part_X - 1]
            minRightX = float('inf') if part_X == l1 else nums1[part_X]

            maxLeftY = float('-inf') if part_Y == 0 else nums2[part_Y - 1]
            minRightY = float('inf') if part_Y == l2 else nums2[part_Y]

            if maxLeftX <= minRightY and maxLeftY <= minRightX:
                if (l1 + l2) % 2 == 0:
                    return (max(maxLeftX, maxLeftY) + min(minRightX, minRightY)) / 2.0
                else:
                    return max(maxLeftX, maxLeftY)
            
            elif maxLeftX > minRightY:
                right = part_X - 1
            else:
                left = part_X + 1
        
        return 0
