class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        ans, sol = [], []

        def backtrack(i, summ):
            if summ == target:
                ans.append(sol[:])
                return
            
            if summ > target or i == len(nums):
                return

            # don't use nums[i]
            backtrack(i+1, summ)

            # use nums[i]
            sol.append(nums[i])
            backtrack(i, summ+nums[i])
            sol.pop()
        
        backtrack(0, 0)
        return ans
