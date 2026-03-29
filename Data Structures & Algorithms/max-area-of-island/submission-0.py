class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        maxArea, area = 0, [0]

        def dfs(i, j):
            if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] != 1:
                return
            else:
                grid[i][j] = 0
                area[0] += 1

                dfs(i+1, j)
                dfs(i-1, j)
                dfs(i, j+1)
                dfs(i, j-1)
            

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    dfs(i, j)
                    maxArea = max(maxArea, area[0])
                    area[0] = 0
        
        return maxArea