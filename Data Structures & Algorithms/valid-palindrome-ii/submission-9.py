class Solution:
    def validPalindrome(self, s: str) -> bool:
        # 2 pointers

        if len(s) <= 2: return True
        if len(s) == 3: return s[0] == s[2]

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


        '''
        # BRUTE FORCE

        if len(s) <= 2: return True
        if len(s) == 3: return s[0] == s[2]

        def isPal(temp):
            return temp == temp[::-1]
        
        if isPal(s[1:]) or isPal(s[:len(s)-1]): return True

        for i in range(1, len(s) - 1):
            temp = s[:i] + s[i+1:]

            if isPal(temp): return True

        return False  
        '''      