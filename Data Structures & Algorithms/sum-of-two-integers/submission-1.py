class Solution:
    def getSum(self, a: int, b: int) -> int:
        mask = 0xFFFFFFFF
        max_int = 0x7FFFFFFF # 32-bit of all 1's
        res = 0
        carry = 0

        while b != 0:
            carry = (a & b) << 1
            a = (a ^ b) & mask 
            b = carry & mask # when there are no more carries left, we can end
        
        return a if a <= max_int else ~(a ^ mask)
        
