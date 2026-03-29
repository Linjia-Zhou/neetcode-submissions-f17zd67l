class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums) == 1: return nums[0]
        
        l, r = 0, 1
        curSum, maxSum = nums[l], nums[l]

        while r < len(nums):
            print(l, r)
            if curSum + nums[r] < nums[r]:
                curSum = nums[r]
                l = r
                r += 1
            else:
                curSum += nums[r]
                r += 1
            maxSum = max(maxSum, curSum)
        return maxSum