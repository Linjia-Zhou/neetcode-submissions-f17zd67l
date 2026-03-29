class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_s = ''

        for ch in s:
            if ch.isalnum():
                new_s += ch

        start, end = 0, len(new_s)-1
        print(new_s)
        while start < end:
            print(new_s[start] + ' ' + new_s[end])
            if new_s[start].lower() != new_s[end].lower():
                return False
            start += 1
            end -= 1
        
        return True