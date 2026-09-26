class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        p = strs[0]

        for s in strs[1:]:
            i = 0
            
            while i < min(len(p), len(s)) and s[i] == p[i]:
                i += 1
            
            p = p[:i]

            if p == '': return p
            
        return p