import random

class Solution:
    def __init__(self, w: List[int]):
        self.w = w

    def pickIndex(self) -> int:
        sumArr = self.w[:]

        for i in range(1, len(self.w)):
            sumArr[i] += sumArr[i-1]
        
        n = random.randint(1, sumArr[-1])
        l, r = 0, len(sumArr)-1
        ans = 0

        while l <= r:
            m = (l + r) // 2

            if sumArr[m] == n:
                return m
            elif sumArr[m] > n:
                ans = m
                r = m - 1
            else:
                l = m + 1
        
        return ans



        
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()