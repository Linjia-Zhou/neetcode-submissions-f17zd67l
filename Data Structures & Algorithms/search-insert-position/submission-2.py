class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        nums.sort()
        l, r = 0, len(nums)-1

        while l <= r:
            if nums[l] == target: return l
            if nums[r] == target: return r

            if nums[l] > target: return l
            if nums[r] < target: return r + 1

            l += 1
            r -= 1
        
        return min(r, l) + 1
    

    # nums=[1,3,5,6], target = 2
    
    # l = 0, r = 3
    # nums[0] = 1, nums[3] = 6

    # l = 1, r = 2
    # nums[1] = 3, nums[2] = 5
