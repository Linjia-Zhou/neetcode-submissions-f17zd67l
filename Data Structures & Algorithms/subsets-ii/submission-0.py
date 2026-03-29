class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = []

        def backtrack(i, sol):
            # base case
            if i == len(nums):
                ans.append(sol[:])
                return
            
            # recursive case
            # choose nums[i]
            sol.append(nums[i])
            backtrack(i+1, sol)
            sol.pop()

            # don't choose nums[i]
            while i + 1 < len(nums) and nums[i] == nums[i+1]: # skip over all duplicates
                i += 1
            backtrack(i+1, sol)
        
        backtrack(0, [])
        return ans
