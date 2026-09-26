class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        temp = s.rstrip()
        i = len(temp) - 1
        ans = 0

        while i >= 0 and temp[i] != ' ':
            ans += 1
            i -= 1
        
        return ans



        
        
