class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0: return 0
        if x == 1 or x == 2 or x == 3: return 1

        ans = 0

        for i in range(2, x//2 + 1):
            if i * i == x: return i
            if i * i > x: return ans
            if i * i < x: ans = i
        
        return ans

# x = 13
# i in range(2, 7)

# i = 2
# i * i = 4
# ans = 2

# i = 3
# i * i = 9
# ans = 3

# i = 4
# i * i = 16 -> return ans (3)




