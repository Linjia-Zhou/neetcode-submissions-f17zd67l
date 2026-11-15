class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        sett = set(allowed)
        ans = 0

        for w in words:
            good = True
            for c in w:
                if c not in sett:
                    good = False
                    break
            
            if good: ans += 1
        
        return ans