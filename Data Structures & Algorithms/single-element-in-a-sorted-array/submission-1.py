class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        # brute force
        if len(nums) == 1: return nums[0]

        l, r = 0, len(nums)-1

        while l <= r:
            if nums[l] == nums[l + 1]:
                l += 2
            else:
                return nums[l]
            
            if nums[r] == nums[r - 1]:
                r -= 2
            else:
                return nums[r]

