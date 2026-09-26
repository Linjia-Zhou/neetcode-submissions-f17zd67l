class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        p = strs[0]

        for s in strs:
            if len(s) < len(p): p = s
        
        # now, p is the shortest string in strs, which is the maximum possible common prefix

        for s in strs:
            for i in range(len(p) - 1, -1, -1):
                if s[i] != p[i]:
                    p = p[:i]
        
        return p