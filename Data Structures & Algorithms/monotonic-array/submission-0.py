class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        def inc(k):
            for i in range(k, len(nums)-1):
                if nums[i] > nums[i+1]: return False
            return True
        
        def dec(k):
            for i in range(k, len(nums)-1):
                if nums[i] < nums[i+1]: return False
            return True

        k = 0
        while k < len(nums) - 1 and nums[k] == nums[k+1]: k += 1
        if k == len(nums) - 1: return True

        if nums[k] < nums[k+1]: return inc(k)
        else: return dec(k)


        

