class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        # binary search
        l, r = 0, len(nums)-1

        while l <= r:
            m = (l + r) // 2# l + ((r - l) // 2)

            if nums[m] == target: return True

            if nums[m] > nums[l]: # left side is sorted
                if nums[l] <= target < nums[m]:
                    r = m - 1
                else:
                    l = m + 1
            elif nums[m] < nums[l]: # right side is sorted
                if nums[m] < target <= nums[r]: 
                    l = m + 1
                else:
                    r = m - 1
            else: # if nums[m] == nums[l] or nums[r], then we can't determine which side is sorted
                l += 1
        
        return False
