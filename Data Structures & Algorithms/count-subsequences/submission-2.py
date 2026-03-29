class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        memo = {}

        def dfs(i, j):
            # base cases
            if j == len(t): return 1
            if i == len(s): return 0
            if (i, j) in memo: return memo[(i, j)]

            # recursive cases
            res = 0
            if s[i] == t[j]:
                res += dfs(i+1, j+1)
            
            res += dfs(i+1, j) # always need to check i+1, even if s[i] == j[i]

            memo[(i, j)] = res
            return memo[(i, j)]
        
        return dfs(0, 0)