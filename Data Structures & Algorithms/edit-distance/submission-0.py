class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        if len(word2) == 0: return len(word1)

        memo = {} # (i, j): num of operations to get word2 from here

        def dfs(i, j):
            # base cases
            if i == len(word1):
                return len(word2) - j
            if j == len(word2):
                return len(word1) - i
            if (i, j) in memo:
                return memo[(i, j)]

            # recursive cases
            if word1[i] == word2[j]:
                memo[(i, j)] = dfs(i+1, j+1)
            else:
                memo[(i, j)] = 1 + min(dfs(i+1, j), dfs(i, j+1), dfs(i+1, j+1))
            
            return memo[(i, j)]
        
        return dfs(0, 0)
            
