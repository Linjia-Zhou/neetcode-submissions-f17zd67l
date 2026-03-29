class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ans = 0

        # this function is turning the entire island into 0's
        def dfs(i, j):
            if i >= len(grid) or i < 0 or j >= len(grid[0]) or j < 0 or grid[i][j] != '1':
                return 
            else:
                grid[i][j] = '0'
                dfs(i, j+1)
                dfs(i, j-1)
                dfs(i+1, j)
                dfs(i-1, j)

        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    ans += 1
                    dfs(i, j)
        
        return ans