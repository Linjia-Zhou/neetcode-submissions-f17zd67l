class Solution:
    def findMin(self, nums: List[int]) -> int:
        res = nums[0]
        l, r = 0, len(nums)-1

        while l <= r:
            mid = (l+r)//2
            if nums[l] <= nums[r]:
                res = min(res, nums[l])

            if nums[mid] >= nums[l]: # nums[mid] in same section as nums[l]
                res = min(res, nums[mid])
                l = mid+1
            else: # nums[mid] in same section as nums[r]
                res = min(res, nums[mid])
                r = mid-1
        
        return res
            
            
