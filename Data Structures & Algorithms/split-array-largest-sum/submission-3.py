class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        # binary search
        def is_valid_sum(m):
            temp_sum = 0
            temp_k = k 
            i = 0

            while temp_k > 0 and i < len(nums):
                temp_sum += nums[i]

                if temp_sum == m:
                    temp_k -= 1
                    temp_sum = 0
                    i += 1
                elif temp_sum > m:
                    temp_k -= 1
                    temp_sum = 0
                else:
                    i += 1

            # found valid sum
            return temp_k >= 0 and i >= len(nums) 

        l = max(nums) # minimum possible answer
        r = sum(nums) # maximum possible answer
        res = r

        while l <= r:
            m = (l + r) // 2 # possible sum we're currently testing
            
            if is_valid_sum(m): # found valid sum
                res = min(res, m)
                r = m - 1 # see if we can find an even smaller sum
            else:
                l = m + 1
        return res



            
