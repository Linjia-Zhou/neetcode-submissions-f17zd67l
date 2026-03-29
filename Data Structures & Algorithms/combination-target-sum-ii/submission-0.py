class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        candidates.sort()

        def backtrack(i, sol, summ):
            # base cases
            if summ == target:
                ans.append(sol[:])
                return
            
            if summ > target or i == len(candidates):
                return
            
            # recursive case

            # choose current number
            sol.append(candidates[i])
            backtrack(i+1, sol, summ+candidates[i])
            sol.pop() # need to remove the number we just added b/c our next call is NOT including current number

            # don't choose current number
            # we need to skip ALL instances of this number, so need to skip over all duplicates
            # we've already gone through steps to include all these duplicates in prev recursive call

            while i + 1 < len(candidates) and candidates[i] == candidates[i+1]: 
                i += 1
            backtrack(i+1, sol, summ)
        
        backtrack(0, [], 0)
        return ans