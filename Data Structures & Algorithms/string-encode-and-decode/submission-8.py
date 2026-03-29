class Solution:

    def encode(self, strs: List[str]) -> str:
        ans = ''
        for s in strs:
            ans = ans + str(len(s)) + '#' + s

        return ans

    def decode(self, s: str) -> List[str]:
        ans = []
        i = 0
        while i < len(s):
            anchor = i
            while s[anchor] != '#':
                anchor += 1

            length = int(s[i:anchor])
            i = anchor + 1
            anchor = i + length
            ans.append(s[i:anchor])
            i = anchor 
                
        return ans