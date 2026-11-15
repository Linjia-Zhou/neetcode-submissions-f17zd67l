class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        d = Counter(magazine)

        for c in ransomNote:
            if c not in magazine or d[c] == 0:
                return False
            else:
                d[c] -= 1
        
        return True