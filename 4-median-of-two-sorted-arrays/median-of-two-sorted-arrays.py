class Solution:
    def findMedianSortedArrays(self, num1: List[int], num2: List[int]) -> float:
        num1.extend(num2)
        num1.sort()
        l=len(num1)
        if l%2==1:
            return num1[l//2]
        else:
            return (num1[l//2]+num1[l//2-1])/2