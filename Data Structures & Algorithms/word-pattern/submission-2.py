class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        p = 0
        i = 0
        p_s = {}
        s_p = {}

        while i < len(s) and p < len(pattern):
            space = s.find(' ', i, len(s))
            word = s[i:space] if space != -1 else s[i:]
            ch = pattern[p]

            if ch in p_s:
                if p_s[ch] != word: return False
            
            if word in s_p:
                if s_p[word] != ch: return False
            
            p_s[ch] = word
            s_p[word] = ch
            
            i = space + 1 if space != -1 else len(s)
            p += 1
        
        return i >= len(s) and p >= len(pattern)
