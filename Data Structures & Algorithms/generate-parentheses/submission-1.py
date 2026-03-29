class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []

        def backtrack(n_open, n_close, s):
            # base case
            if n_open + n_close == n * 2:
                ans.append(s)
                return
            
            # recursive case

            if len(s) == 0 or n_close == n or n_open == n_close: # must add open parenthesis
                backtrack(n_open + 1, n_close, s + '(')
                s = s[:-1]
            
            elif n_open == n: # must add close parenthesis
                backtrack(n_open, n_close + 1, s + ')')
                s = s[:-1]
            
            else:
                backtrack(n_open + 1, n_close, s + '(')
                backtrack(n_open, n_close + 1, s + ')')
                s = s[:-1]
        
        backtrack(0, 0, '')
        return ans

            

