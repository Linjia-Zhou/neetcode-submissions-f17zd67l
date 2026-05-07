class Solution:
    def arrangeCoins(self, n: int) -> int:
        l, r = 0, n

        while l <= r:
            m = (l + r) // 2 # test this as the output
            summ = (m * (m + 1)) // 2
            if summ == n:
                return m
            elif summ > n:
                r = m - 1
            else:
                l = m + 1
        
        return (l + r) // 2

