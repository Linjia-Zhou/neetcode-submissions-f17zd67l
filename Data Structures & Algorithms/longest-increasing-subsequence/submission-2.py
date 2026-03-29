class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [1] * len(nums) # represents the longest subsequence ending at index i

        for i in range(1, len(nums)): # start at index 1 b/c index 0 is guaranteed to only have subsequence of length 1
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[j] + 1, dp[i])

        return max(dp)


                
                






            

            

