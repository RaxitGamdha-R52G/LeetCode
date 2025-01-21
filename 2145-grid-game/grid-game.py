class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:
        n = len(grid[0])
        
        for i in range(1, n):
            grid[0][i] = grid[0][i - 1] + grid[0][i]
            grid[1][i] = grid[1][i - 1] + grid[1][i]
        
        points = float('inf')
        
        for i in range(n):
            points_top = grid[0][n - 1] - grid[0][i]
            points_bottom = grid[1][i - 1] if i > 0 else 0
            
            
            points_second = max(points_top, points_bottom)
            
            points = min(points, points_second)
        
        return points
