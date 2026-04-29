class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        # binary search
        # KEY POINT: len(nums) must always be odd, if there are only pairs plus 1 single value
        if len(nums) == 1: return nums[0]

        l, r = 0, len(nums)-1

        while l <= r:
            m = (l + r) // 2

            if (m == len(nums) - 1 and nums[m] != nums[m - 1]) or (m == 0 and nums[m] != nums[m+1]) or (m > 0 and m < len(nums)-1 and nums[m] != nums[m - 1] and nums[m] != nums[m + 1]):
                return nums[m]
            else:
                left_side = m if nums[m] == nums[m-1] else m - 1
                if left_side % 2 == 0: # left side is odd, answer must be here
                    r = left_side
                else: # left side is even, answer must be on the right
                    l = m + 1

