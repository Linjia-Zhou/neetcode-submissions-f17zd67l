class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        ans = []
        digit_map = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}

        def backtrack(i, s):
            if len(s) == len(digits):
                ans.append(s)
                return
            
            letters = digit_map[digits[i]] # ex. if digit_map[i] = 3, then letters = 'def'
            for char in letters:
                backtrack(i+1, s + char)
        

        if digits: backtrack(0, '')
        return ans


        
