class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix:
            return False  
        d = False
        n = len(matrix[0])
        left = 0
        right = len(matrix)-1
        mid_a = 0          
        while left <= right:
            mid = (left+right)//2
            if d and matrix[mid_a][mid] == target:
                return True
            elif d and matrix[mid_a][mid] < target:
                left = mid + 1
            elif d and matrix[mid_a][mid] > target:
                right = mid - 1
            elif matrix[mid][0] <= target <= matrix[mid][n-1]:
                right = n-1
                left = 0
                d = True
                mid_a = mid
            elif matrix[mid][0] > target:
                right = mid -1
            else:
                left = mid + 1
        
        return False