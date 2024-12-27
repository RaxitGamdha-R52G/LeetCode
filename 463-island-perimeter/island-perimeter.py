class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        per = 0
        x_l = len(grid)
        y_l = len(grid[0])
        for i in range(x_l):
            for j in range(y_l):
                if grid[i][j] == 1:
                    for x,y in [(-1,0),(0,-1),(1,0),(0,1)]:
                        t_x = i + x
                        t_y = j + y
                        if 0 <= t_x < x_l and 0 <= t_y < y_l and grid[t_x][t_y] == 1:
                            pass
                        else:
                            per += 1
        return per