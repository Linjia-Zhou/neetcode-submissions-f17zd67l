class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n = int("".join(map(str, digits)))
        n += 1

        ans = []
        for ch in str(n):
            ans.append(int(ch))
        
        return ans