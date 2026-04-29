class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        if len(nums) == 1: return 0
        if len(nums) == 2:
            if nums[0] > nums[1]: return 0
            else: return 1
            
        def isPeak(i) -> bool:
            # returns if index i is a peak
            if i == 0:
                return nums[i] > nums[i+1]
            
            if i == len(nums) - 1:
                return nums[i] > nums[i-1]
            
            return nums[i] > nums[i-1] and nums[i] > nums[i+1]


        l, r = 0, len(nums)-1

        while l <= r:
            m = (l + r) // 2

            # checking peak
            if isPeak(m): return m
            if isPeak(l): return l
            if isPeak(r): return r
            
            # peak not found
            if nums[m] <= nums[l]: # m is on right side, shift r to left
                r = m - 1
            elif nums[m] <= nums[r]: # m is on left side, shift l to right
                l = m + 1
            else:
                l += 1
                r -= 1
        

            