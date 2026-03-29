class Solution:
    def findMin(self, nums: List[int]) -> int:
        res = nums[0]
        res_index = 0
        l, r = 0, len(nums)-1

        while l <= r:
            mid = (l+r)//2
            if nums[l] <= nums[r]:
                if nums[l] < res: 
                    res = nums[l]
                    res_index = l

            if nums[mid] >= nums[l]: # nums[mid] in same section as nums[l]
                if nums[mid] < res:
                    res = nums[mid]
                    res_index = mid
                l = mid+1
            else: # nums[mid] in same section as nums[r]
                if nums[mid] < res:
                    res = nums[mid]
                    res_index = mid
                r = mid-1
        
        return res_index

    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)-1
        min_index = self.findMin(nums)

        if min_index == 0:
            l, r = 0, len(nums)-1
        elif target >= nums[0] and target <= nums[min_index-1]: # left side
            l, r = 0, min_index-1
        else: # right side
            l, r = min_index, len(nums)-1
        
        while l <= r:
            m = (l+r) // 2

            if nums[m] == target:
                return m
            elif nums[m] < target:
                l = m + 1
            else:
                r = m -1
        
        return -1



                