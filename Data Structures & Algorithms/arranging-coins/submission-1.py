class Solution:
    def arrangeCoins(self, n: int) -> int:
        # n: 1, ans: 1
        # n: 2, ans: 1
        # n: 3, ans: 2
        # n: 4, ans: 2
        # n: 5, ans: 2
        # n: 6, ans: 3
        # n: 7, ans: 3
        # n: 8, ans: 3
        # n: 9, ans: 3
        # n: 10, ans: 4

        l, r = 0, n
        m = 0

        while l <= r:
            m = (l + r) // 2 # test this as the output
            summ = (m * (m + 1)) / 2
            if summ == n:
                return m
            elif summ > n:
                r = m - 1
            else:
                l = m + 1
        
        return (l + r) // 2

