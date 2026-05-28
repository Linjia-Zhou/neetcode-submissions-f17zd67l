import random

class Solution:
    def __init__(self, w: List[int]):
        self.w = w
        self.sumArr = w[:]
        for i in range(1, len(self.w)):
            self.sumArr[i] += self.sumArr[i-1]

    def pickIndex(self) -> int:
        n = random.randint(1, self.sumArr[-1])
        l, r = 0, len(self.sumArr)-1
        ans = 0

        while l <= r:
            m = (l + r) // 2

            if self.sumArr[m] >= n:
                ans = m
                r = m - 1
            else:
                l = m + 1
        
        return ans



        
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()