class Solution:
    def validPalindrome(self, s: str) -> bool:
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
        if len(s) <= 2: return True
        if len(s) == 3: return s[0] == s[2]

        # abcca
        # accba

        count = 0 # counts how many characters are not the same
        l, r = 0, len(s) - 1

        while l < r: 
            if s[l] != s[r]: 
                count += 1
            l += 1
            r -= 1
        
        if len(s) % 2 != 0: # odd length, so need to check middle character
            if s[l] != s[l-1] and s[l] != s[l+1]: # middle value is not equal to either neighbour
                count += 1

        return count <= 1
        '''