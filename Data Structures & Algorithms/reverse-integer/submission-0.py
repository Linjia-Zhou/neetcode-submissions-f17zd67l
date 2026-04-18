class Solution:
    def reverse(self, x: int) -> int:
        max_int = 0x7FFFFFFF
        min_int = -0x80000000
        mask = 0xFFFFFFFF
        ans = 0

        str_x = str(x)

        if x < 0: 
            str_x = str_x[::-1]
            ans = -int(str_x[:-1])
        else:
            ans = int(str_x[::-1])
        
        if ans < min_int or ans > max_int: return 0
        else: return ans


        
