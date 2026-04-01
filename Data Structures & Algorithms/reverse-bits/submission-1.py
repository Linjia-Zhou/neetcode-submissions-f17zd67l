class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0

        # n = 1010, range = 4
        # i = 0
            # bit = (1010 >> 0) & 1 = 0 ;
            # res = 0 + (0 << (3 - 0)) = 0 + 0000 = 0000
        # i = 1
            # bit = (1010 >> 1) & 1 = 0101 & 1 = 1
            # res = 0 + (1 << (3-1)) = 0 + 100 = 100
        # i = 2
            # bit = (1010 >> 2) & 1 = 0010 & 1 = 0
            # res = 100 + (0 << (3-2)) = 100 + 00 = 100
        # i = 3
            # bit = (1010 >> 3) & 1 = 0001 & 1 = 1
            # res = 100 + (1 << (3-3)) = 100 + 1 = 101

        for i in range(32):
            bit = (n >> i) & 1 # this gives us the last digit in n until all digits in n are 0
            res = res + (bit << (31-i)) # shifts bit to correct position in res
        
        return res
        
        

