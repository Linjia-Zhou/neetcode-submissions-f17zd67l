class Solution:
    def climbStairs(self, n: int) -> int:
        cache = collections.defaultdict()
        cache[1] = 1 # {1:1}
        cache[2] = 2 # {1:1, 2:2}

        def recursion(i):
            if i in cache: 
                return cache[i]
            else:
                cache[i] = recursion(i-1) + recursion(i-2)
                return cache[i]
        
        return recursion(n)








            

        

            

