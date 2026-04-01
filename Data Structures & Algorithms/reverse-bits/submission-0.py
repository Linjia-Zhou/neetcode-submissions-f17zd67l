class Solution:
    def reverseBits(self, n: int) -> int:
        res = ''

        for i in range(32):
            bit = (n >> i) & 1 # this gives us the last digit in n until all digits in n are 0
            res += str(bit)
        
        return int(res, 2)
        

