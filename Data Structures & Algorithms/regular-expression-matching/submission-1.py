class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        memo = {} # (i, j): T/F can we get s[:i+1] == p[:j+1]

        def dfs(i, j):
            if i >= len(s) and j >= len(p): return True
            if j >= len(p): return False # ran out of characters in p to match to s

            if (i, j) in memo: return memo[(i, j)]
            
            match = i < len(s) and (s[i] == p[j] or p[j] == '.')

            if j < len(p) - 1 and p[j+1] == '*':
                use_star = match and dfs(i+1, j) # don't wanna use star if s[i] != p[j]
                no_star = dfs(i, j+2)
                memo[(i, j)] = use_star or no_star
                return memo[(i, j)]
            if match:
                memo[(i, j)] = dfs(i+1, j+1)
                return memo[(i, j)]

            memo[(i, j)] = False
            return memo[(i, j)]
        
        return dfs(0, 0)

        
            




