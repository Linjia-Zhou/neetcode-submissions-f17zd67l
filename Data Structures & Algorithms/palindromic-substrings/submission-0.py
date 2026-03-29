class Solution:
    def countSubstrings(self, s: str) -> int:

        def rec(start, i, count):
            if i >= len(s):
                return count
            
            curr_string = s[start:i+1]

            if curr_string == curr_string[::-1]:
                count += 1
            
            return rec(start, i+1, count)
        
        ans = 0
        for i in range(len(s)):
            ans += rec(i, i, 0)
        
        return ans
