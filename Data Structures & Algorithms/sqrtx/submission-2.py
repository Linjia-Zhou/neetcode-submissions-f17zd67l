class Solution:
    def mySqrt(self, x: int) -> int:
        l, r = 0, x
        ans = 0

        while l <= r:
            m = (l + r) // 2
            
            if m * m == x: return m
            
            if m * m > x:
                r = m - 1
            
            if m * m < x:
                ans = m
                l = m + 1

        return ans




