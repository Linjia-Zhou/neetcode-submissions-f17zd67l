class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans, sol = [], []

        def backtrack():
            # base case
            if len(sol) == len(nums):
                ans.append(sol[:])
                return
            
            # recursive case
            for num in nums:
                if num not in sol:
                    sol.append(num)
                    backtrack()
                    sol.pop()

        backtrack()
        return ans