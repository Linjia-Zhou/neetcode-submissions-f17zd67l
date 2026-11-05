class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        def inc(i):
            count = 1
            while i < len(nums) - 1 and nums[i+1] > nums[i]:
                count += 1
                i += 1
            
            return count
        
        def dec(i):
            count = 1
            while i < len(nums) - 1 and nums[i+1] < nums[i]:
                count += 1
                i += 1
            
            return count

        ans = 1
        for i in range(len(nums)-1):
            ans = max(ans, inc(i), dec(i))
        
        return ans