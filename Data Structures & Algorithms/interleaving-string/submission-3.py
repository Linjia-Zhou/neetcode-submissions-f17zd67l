class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3): return False
        memo = {} # (i, j): T/F if we can reach s3 from this index combo

        def dfs(i, j, k):
            # base cases
            if i == len(s1) and j == len(s2) and k == len(s3): 
                return True

            if (i, j) in memo:
                return memo[(i, j)]

            # recursive cases
            res = False
            if i < len(s1) and s1[i] == s3[k]:
                res = dfs(i+1, j, k+1)

            if not res and j < len(s2) and s2[j] == s3[k]: # if prev recursion call fails come here
                res = dfs(i, j+1, k+1)
            
            memo[(i, j)] = res
            return memo[(i, j)]
        
        return dfs(0, 0, 0)
