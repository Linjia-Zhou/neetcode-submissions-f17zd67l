class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        before = [1] * len(nums) # index i will store product of all values AFTER nums[i]
        after = [1] * len(nums)
        prod = 1

        for i in range(len(nums)-1):
            prod = nums[i] * prod
            before[i+1] = prod

        prod = 1
        for i in range(len(nums)-1, 0, -1):
            prod = nums[i] * prod
            after[i-1] = prod

        print(before)
        print(after)
        ans = [0] * len(nums)
        for i in range(len(nums)):
            ans[i] = before[i] * after[i]
        
        return ans