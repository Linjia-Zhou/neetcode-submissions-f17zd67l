class Solution:
    def validPalindrome(self, s: str) -> bool:
        def isPal(temp):
            return temp == temp[::-1]
        
        if isPal(s): return True

        l, r = 0, len(s) - 1
        
        while l < r:
            if s[l] != s[r]:
                s_remove_l = s[:l] + s[l+1:] if l > 0 else s[l+1:]
                s_remove_r = s[:r] + s[r+1:] if r < len(s) - 1 else s[:r]

                if isPal(s_remove_l) or isPal(s_remove_r): return True
            
            l += 1
            r -= 1
        
        return False