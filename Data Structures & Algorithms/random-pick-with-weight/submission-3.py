import random, bisect

class Solution:
    def __init__(self, w: List[int]):
        self.w = w
        self.sumArr = w[:]
        for i in range(1, len(self.w)):
            self.sumArr[i] += self.sumArr[i-1]

    def pickIndex(self) -> int:
        n = random.randint(1, self.sumArr[-1])
        return bisect.bisect_left(self.sumArr, n)



        
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()