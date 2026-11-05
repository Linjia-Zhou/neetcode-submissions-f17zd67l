class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        count = ans = nums[0]

        for i in range(1, len(nums)):
            if nums[i] > nums[i-1]:
                count += nums[i]
            else:
                count = nums[i]
            
            ans = max(ans, count)
        
        return ans
