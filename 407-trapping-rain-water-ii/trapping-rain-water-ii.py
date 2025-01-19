class Solution:
    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        area = 0
        m, n = len(heightMap),len(heightMap[0])
        visited = [[False] * n for _ in range(m)]

        heightArr = []
        for i in range(m):
            for j in range(n):
                if i == 0 or i == m - 1 or j == 0 or j == n - 1:
                    heapq.heappush(heightArr, (heightMap[i][j], i, j))
                    visited[i][j] = True
        
        directions = [(-1,0),(1,0),(0,-1),(0,1)]
        while heightArr:
            height, x, y = heapq.heappop(heightArr)

            for dx, dy in directions:
                nx, ny = dx + x, dy + y

                if 0<= nx < m and 0 <= ny < n and not visited[nx][ny]:
                    area += max(0, height - heightMap[nx][ny])
                    heapq.heappush(heightArr, (max(height, heightMap[nx][ny]), nx, ny))
                    visited[nx][ny] = True
        return area