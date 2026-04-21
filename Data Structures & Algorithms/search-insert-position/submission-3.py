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
