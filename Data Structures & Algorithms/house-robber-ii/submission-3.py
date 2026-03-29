class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1: return nums[0]

        cache = [-1] * len(nums)

        def rob1(nums):
            cache = [-1] * len(nums)

            def rec(i):
                if i >= len(nums):
                    return 0
                if cache[i] == -1:
                    cache[i] = nums[i] + max(rec(i+2), rec(i+3))
                return cache[i]
                
            return max(rec(0), rec(1))
        
        return max(rob1(nums[:-1]), rob1(nums[1:]))



