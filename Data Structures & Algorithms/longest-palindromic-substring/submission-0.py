class Solution:
    def longestPalindrome(self, s: str) -> str:

        def rec(start, i, pal):
            if i >= len(s):
                return pal
            
            curr_string = s[start:i+1]
            print(i, curr_string, pal)

            if curr_string == curr_string[::-1] and len(curr_string) > len(pal):
                pal = curr_string
            
            return rec(start, i+1, pal)
        
        ans = ''

        for i in range(len(s)):
            print('for loop i: ', i)
            curr_ans = rec(i, i, ans)
            # print(curr_ans)
            if len(curr_ans) > len(ans):
                ans = curr_ans
        
        return ans
