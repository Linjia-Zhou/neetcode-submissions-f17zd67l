class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        left = 0
        right = sum(nums[1:])

        if right == 0: return 0 # all right numbers sum to 0, so leftmost pivot is first index

        for i in range(1, len(nums)):
            left += nums[i-1]
            right -= nums[i]

            if left == right: return i
        
        return -1
