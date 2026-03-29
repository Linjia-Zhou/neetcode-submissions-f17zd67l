class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if len(nums) == 1: return True
        if nums[0] == 0: return False

        dp = [True] + ([False] * (len(nums)-1))
        print(dp)

        i = 0
        while i < len(nums)-1:
            n = nums[i]
            if n == 0 and not dp[i+1]:
                return False
            else:
                dp[i+1: i+n+1] = [True] * n
            print(i, n, dp)
            i += 1
            
        return dp[-1]