class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        if len(t) > len(s): return 0

        memo = {} # (s_index, t_index): num of subsequences from this combo

        def dfs(i, j):
            if j == len(t): return 1
            if i == len(s): return 0
            if (i, j) in memo: return memo[(i, j)]
            
            res = dfs(i+1, j) # must always consider skipping the current character
            if s[i] == t[j]:
                res += dfs(i+1, j+1)
            
            memo[(i, j)] = res
            return memo[(i, j)]
        
        return dfs(0, 0)