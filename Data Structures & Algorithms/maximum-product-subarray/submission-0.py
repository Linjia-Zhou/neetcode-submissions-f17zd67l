class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        ans = max(nums)
        curr_max, curr_min = 1, 1

        for n in nums:
            if n == 0:
                curr_max, curr_min = 1, 1
                continue
            
            tmp = curr_max * n # need temp variable in case curr_max changes before curr_min

            curr_max = max(curr_max * n, curr_min * n, n)
            curr_min = min(tmp, curr_min * n, n)

            ans = max(ans, curr_max, curr_min)
        
        return ans
        


        
