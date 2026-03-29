from collections import defaultdict 
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        longest = 0
        hm = {}
        l = 0

        for r in range(len(s)):
            if s[r] in hm:
                l = max(hm[s[r]] + 1, l) # need max b/c first instance of s[r] could occur before our current l
            hm[s[r]] = r
            longest = max(r-l+1, longest)
        
        return longest
            

                

        
