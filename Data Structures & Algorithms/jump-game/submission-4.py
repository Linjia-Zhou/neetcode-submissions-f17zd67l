class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if len(nums) == 1: return True
        if nums[0] == 0: return False

        dp = [True] + ([False] * (len(nums)-1))

        for i in range(len(nums)-1):
            n = nums[i]
            if n == 0 and not dp[i+1]:
                return False
            else:
                dp[i+1: i+n+1] = [True] * n
            
        return dp[-1]