class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        inc, dec = True, True # tracks if nums can still be increasing or decreasing

        for i in range(len(nums)-1):
            if nums[i] > nums[i+1]: # nums can no longer be increasing (non-decreasing)
                inc = False
            if nums[i] < nums[i+1]: # nums can no longer be decreasing (non-increasing)
                dec = False
        
        return inc or dec
