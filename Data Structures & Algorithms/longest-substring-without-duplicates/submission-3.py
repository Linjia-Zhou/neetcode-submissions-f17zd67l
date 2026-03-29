from collections import defaultdict 
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        # {'a': 0, 'b': 1}
        # l = 0
        # r = 2
        longest = 0
        hm = {}
        l = 0

        for r in range(len(s)):
            if s[r] in hm:
                l = max(hm[s[r]] + 1, l)
            hm[s[r]] = r
            longest = max(r-l+1, longest)
        
        return longest
            

                

        
