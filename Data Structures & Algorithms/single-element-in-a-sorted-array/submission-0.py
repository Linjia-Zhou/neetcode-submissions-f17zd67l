class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        if len(nums) == 1: return nums[0]
        # len(nums) must always be odd, if there are only pairs plus 1 single value

        l, r = 0, len(nums)-1

        # nums = [3,3,7,7,10,11,11]
        # bin = [0,0,0,0,1,0,0]
        # if nums[m] == 0, how to change l and r?

        while l <= r:
            if nums[l] == nums[l + 1]:
                l += 2
            else:
                return nums[l]
            
            if nums[r] == nums[r - 1]:
                r -= 2
            else:
                return nums[r]

