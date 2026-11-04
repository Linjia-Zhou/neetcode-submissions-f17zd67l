import math
from collections import defaultdict

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        maj = math.ceil(len(nums)/2)
        d = defaultdict()

        for n in nums:
            if n in d:
                d[n] += 1
            else:
                d[n] = 1
            if d[n] >= maj: 
                    return n
        print(d)
         

