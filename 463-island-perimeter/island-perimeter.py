class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        arr = []
        if not grid:
            return 0
        
        def dfs(grid,i,j,arr):
            x_l = len(grid)
            y_l = len(grid[0])
            arr.append((i,j))
            per = 0
            directions = [(-1,0),(0,-1),(1,0),(0,1)]

            for dx,dy in directions:
                t_x = i + dx
                t_y = j + dy
                if 0 <= t_x < x_l and 0 <= t_y < y_l and grid[t_x][t_y] == 1:
                    if (t_x,t_y) not in arr:
                        per += dfs(grid, t_x, t_y,arr)
                else:
                    per += 1
            return per


        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    return dfs(grid,i,j,arr)
        