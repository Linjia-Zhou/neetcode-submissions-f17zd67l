class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        cache = {(0, 0): 1} # from (i, j), num of unique paths to target grid

        # for i in range(m-1):
        #     for j in range(n-1):
        #         cache[(i, j)] = 1

        def dfs(i, j):
            if i >= m or i < 0: return 0
            if j >= n or j < 0: return 0

            if (i, j) in cache:
                return cache[(i, j)]
            
            cache[(i, j)] = dfs(i-1, j) + dfs(i, j-1)
            return cache[(i, j)]
        
        dfs(m-1, n-1)
        return cache[(m-1, n-1)]

            
