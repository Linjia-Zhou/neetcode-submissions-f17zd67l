class Solution:
    def check(self, nums: List[int]) -> bool:
        i = 0
        while i < len(nums) - 1 and nums[i] <= nums[i+1]:
            i += 1

        if i == len(nums) - 1: return True
        rotated = nums[i+1:] + nums[:i+1]

        for i in range(len(rotated) - 1):
            if rotated[i] > rotated[i+1]: return False
        
        return True
        

