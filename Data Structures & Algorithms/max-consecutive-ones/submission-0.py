class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        ans, curr = 0, 0

        for n in nums:
            if n == 1:
                curr += 1
            else:
                ans = max(ans, curr)
                curr = 0
        
        return max(ans, curr)