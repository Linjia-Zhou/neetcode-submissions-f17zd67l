class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans, sol = [], [] # ans is final answer, sol is 1 solution that will join together to make a string

        def backtrack(openn, close):
            if len(sol) == 2*n:
                ans.append(''.join(sol))
                return
            
            if openn < n:
                sol.append('(')
                backtrack(openn+1, close)
                sol.pop()
            
            if openn > close:
                sol.append(')')
                backtrack(openn, close+1)
                sol.pop()
        
        backtrack(0, 0)
        return ans