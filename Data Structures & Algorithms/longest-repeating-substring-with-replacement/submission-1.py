from collections import defaultdict
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l, r, res = 0, 0, 0
        hm = defaultdict(int)

        while r < len(s):
            hm[s[r]] += 1
            print(s[r])
            window = r-l+1
            freq = max(hm, key=hm.get)
            
            print(f'r: {r}, l: {l},  hm: {hm}, freq: {freq}')
            
            if (window-hm[freq]) <= k:
                res = max(res, window)
                r += 1
            else:
                hm[s[l]] -= 1
                hm[s[r]] -= 1
                l += 1
            print(f'res: {res}')
        return res
            




        


