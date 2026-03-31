class Solution:
    def hammingWeight(self, n: int) -> int:
        ans = 0

        while n:
            n = n & (n-1) # n - 1 will always get rid of the last 1 in n 
            ans += 1
        
        return ans