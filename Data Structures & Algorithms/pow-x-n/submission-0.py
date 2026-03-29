class Solution:
    def myPow(self, x: float, n: int) -> float:
        if x == 1: return 1
        
        def rec(x, n):
            if x == 0: return 0
            if n == 0: return 1

            ans = rec(x * x, n // 2)
            return x * ans if n % 2 == 1 else ans
        
        ans = rec(x, abs(n))
        return ans if n >= 0 else 1/ans

            



            




        