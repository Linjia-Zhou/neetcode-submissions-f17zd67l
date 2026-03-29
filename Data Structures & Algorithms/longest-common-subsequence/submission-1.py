class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        cache = {} # at index (i, j) what's the longest subsequence

        def dfs(i, j):
            if i >= len(text1) or j >= len(text2):
                return 0

            if (i, j) not in cache:
                if text1[i] == text2[j]:
                    cache[(i, j)] = 1 + dfs(i+1, j+1)
                else:
                    cache[(i, j)] = max(dfs(i, j+1), dfs(i+1, j))
            
            return cache[(i, j)]
        
        dfs(0, 0)
        return max(cache.values())



        

                
