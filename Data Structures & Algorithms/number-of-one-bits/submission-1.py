class Solution:
    def hammingWeight(self, n: int) -> int:
        ans = 0

        while n:
            n = n & (n-1) # n - 1 will get rid of the last 1 in n, so this loop runs until there are no more 1's left
            ans += 1
        
        return ans