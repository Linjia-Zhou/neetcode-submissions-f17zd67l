class Solution:
    def partition(self, s: str) -> List[List[str]]:
        ans, sol = [], []

        def backtrack(i):
            # base case
            if i >= len(s):
                ans.append(sol[:])
                return
            
            # recursive case
            for j in range(i, len(s)):
                substring = s[i:j+1]

                if substring == substring[::-1]:
                    sol.append(substring)
                    backtrack(j+1)
                    sol.pop()
        
        backtrack(0)
        return ans

