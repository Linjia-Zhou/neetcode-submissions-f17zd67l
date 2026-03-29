import math
class Solution:
    def enough_hours(self, piles, h, k):
        for pile in piles:
            hours_needed = math.ceil(pile/k)
            h -= hours_needed
        
        return h >= 0

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        upper = max(piles)
        lower = 1
        k = upper

        while lower <= upper:
            mid = (lower+upper)//2

            if self.enough_hours(piles, h, mid): 
                k = mid
                upper = mid - 1
            else:
                lower = mid + 1
        
        return k

