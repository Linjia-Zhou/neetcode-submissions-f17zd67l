from collections import defaultdict
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s): return ''

        countT, window = defaultdict(int), defaultdict(int)
        res, resLen = [-1, -1], float('infinity')
        l = 0
        print(res)
        for ch in t:
            countT[ch] += 1
        
        have, need = 0, len(countT)

        for r in range(len(s)):
            ch = s[r]
            window[ch] += 1
            
            if (ch in countT) and (window[ch] == countT[ch]):
                have += 1
            
            while have == need: 
                if (r-l+1) < resLen:
                    res = [l, r]
                    resLen = r-l+1
                # while have == need, we want to see how small we can make the window
                window[s[l]] -= 1 # remove leftmost character
                if s[l] in countT and window[s[l]] < countT[s[l]]: # checking if removing the left character unsatisfies the condition
                    have -= 1
                l += 1


        l, r = res 
        return s[l:r+1] if resLen != float('infinity') else ''
        

