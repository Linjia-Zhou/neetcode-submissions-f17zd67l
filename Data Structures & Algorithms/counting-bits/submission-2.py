class Solution:
    def countBits(self, n: int) -> List[int]:
        dp = [0] * (n+1)

        for i in range(1, n+1):
            # i >> 1 (right shift) drops the last bit, giving you the "parent" number whose 1-bit count you already computed. Since shifting right by 1 is the same as integer division by 2, it reuses the previously stored result.
            # i & 1 checks whether the last bit is a 1 or 0 — essentially asking "is this number odd?" If it is, there's one extra 1-bit compared to its parent.
            dp[i] = dp[i >> 1] + (i & 1)

        return dp