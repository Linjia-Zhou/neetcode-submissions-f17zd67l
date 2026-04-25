class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        # binary search
        l = max(weights)
        r = sum(weights)
        ans = r

        def satisfy_condition(cap):
            curr_day_w = 0 # how much weight on the current day
            day_count = 0 # how many days we have taken thus far

            for w in weights:
                    curr_day_w += w

                    if curr_day_w > m:
                        day_count += 1
                        curr_day_w = w

                    if curr_day_w == m:
                        day_count += 1
                        curr_day_w = 0
            
            if curr_day_w > 0: 
                day_count += 1
            
            if day_count <= days: return True
            else: return False

        while l <= r:
            m = (l + r) // 2

            if satisfy_condition(m): 
                ans = min(ans, m)
                r = m - 1
            else:
                l = m + 1
        
        return ans




        