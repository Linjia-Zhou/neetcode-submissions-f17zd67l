class Solution:
    def climbStairs(self, n: int) -> int:
        cache = [-1] * n
        cache[0] = 1

        if n > 1: cache[1] = 2

        def rec(num):
            if num == 1:
                return cache[0]
            if num == 2:
                return cache[1]
            
            if cache[num-1] == -1:
                cache[num-1] = rec(num-1) + rec(num-2)
            
            return cache[num-1]
        
        return rec(n)