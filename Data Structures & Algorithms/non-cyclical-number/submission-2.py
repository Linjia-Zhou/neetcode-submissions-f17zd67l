class Solution:
    def isHappy(self, n: int) -> bool:
        def rec(num, nums: set):
            temp = []
            for ch in str(num):
                temp.append(int(ch))
            
            summ = 0
            for t in temp:
                summ += (t**2)
            
            if summ == 1: return True
            elif summ in nums: return False
            else: 
                nums.add(summ)
                return rec(summ, nums)
        
        return rec(n, set())

